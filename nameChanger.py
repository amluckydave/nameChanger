import os
import sys
import time
import regex as re
import configparser
import images_rc  # QPixmap

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']

from sys import argv, exit
from nameChangerPath import nameChangerPathDef

from invoice_changer import Ui_MainWindow
from aboutme import Ui_about
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QDialog
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QObject
from PyQt5.QtGui import QIcon, QCursor, QPixmap

# 创建一个新的ConfigParser对象
config = configparser.ConfigParser()
addrNameChanger = nameChangerPathDef()

dirName = r'C:\Users'

class SharedParams(QObject):
    def __init__(self):
        super(SharedParams, self).__init__()
        self.pattern = ""
shared_params = SharedParams()


class TaskThread(QThread):  # change to new names thread
    task_completed = pyqtSignal()
    task_progress = pyqtSignal(int)
    task_error = pyqtSignal(str)
    task_hash = pyqtSignal(dict)

    def __init__(self, ):
        super(TaskThread, self).__init__()

    def run(self):
        try:
            pattern = shared_params.pattern
            # 创建一个空的哈希表
            correspondence = {}

            fileNameList = os.listdir(dirName)
            total = len(fileNameList)
            if pattern == "":
                self.task_error.emit(str('Please choose the separator.'))
            rules = re.compile(pattern, re.S)

            # 开始数组循环更改文件名
            for index, filename in enumerate(fileNameList):
                file_suffix = filename.split(".")[-1]

                if file_suffix not in ['pdf', 'ofd', 'jpg' 'jpeg']:
                    raise Exception('This folder exists non-standard format files!')

                newFilenameWoSuffix = ''.join(re.findall(rules, str(filename)))

                if newFilenameWoSuffix:
                    newFilename = newFilenameWoSuffix + '.' + file_suffix
                    newFilenamePath = os.path.join(dirName, newFilename)

                    if os.path.exists(newFilenamePath):
                        os.remove(newFilenamePath)
                    os.rename(os.path.join(dirName, filename), os.path.join(dirName, newFilename))

                    correspondence.update({newFilename: filename})

                progress = int((index + 1) / total * 100)
                time.sleep(0.08)  # Slow down the progressBar
                self.task_progress.emit(progress)
            self.task_hash.emit(correspondence)
            self.task_completed.emit()

        except Exception as e:
            # 如果发生异常，发出错误信号
            self.task_error.emit(str(e))


class TaskThread2(QThread):
    task_completed = pyqtSignal()
    task_progress = pyqtSignal(int)
    task_error = pyqtSignal(str)

    def run(self):
        try:
            # 解析INI文件并创建哈希表
            ini_file_path = addrNameChanger + r'prev_names.ini'
            config.read(ini_file_path, encoding='utf-8')
            correspondence = {}
            for section in config.sections():
                correspondence.update({config[section]['new_name']: config[section]['old_name']})

            fileNameList = os.listdir(dirName)
            total = len(fileNameList)
            # 遍历目标文件夹，根据哈希表还原文件名
            folder_path = dirName  # 替换为你的目标文件夹路径
            for index, filename in enumerate(fileNameList):
                if filename in correspondence:
                    new_file_path = os.path.join(folder_path, filename)
                    old_file_path = os.path.join(folder_path, correspondence[filename])
                    os.rename(new_file_path, old_file_path)

                progress = 100 - int((index + 1) / total * 100)
                time.sleep(0.08)  # Slow down the progressBar
                self.task_progress.emit(progress)
            self.task_completed.emit()

        except Exception as e:
            # 如果发生异常，发出错误信号
            self.task_error.emit(str(e))


class aboutMe(QDialog, Ui_about):
    def __init__(self, parent=None):
        super(aboutMe, self).__init__(parent)
        self.uiAbout = Ui_about()
        self.uiAbout.setupUi(self)

        self.uiAbout.github.setText("<a href='https://github.com/amluckydave'>Visit My Github</a>")
        self.uiAbout.github.setOpenExternalLinks(True)

        # 设置鼠标指针为手型
        self.uiAbout.github.setCursor(QCursor(Qt.PointingHandCursor))

        self.uiAbout.pushButton.clicked.connect(self.accept)


class changerUi(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(changerUi, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('invoiceChanger by EliotXu')
        icon = QIcon(QPixmap(':/favicon.ico'))  # 替换为你的图标文件路径
        self.setWindowIcon(icon)

        font = self.ui.reminderLineEdit.font()
        self.default_font = font
        text = self.ui.reminderLineEdit.text()
        self.default_text = text

        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        self.ui.addrLineEdit.setEnabled(False)
        self.ui.reminderLineEdit.setEnabled(False)
        self.ui.openPushButton.clicked.connect(self.chooseDir)
        self.ui.changePushButton.clicked.connect(self.changeName)

        self.task_thread = TaskThread()
        self.task_thread.task_completed.connect(self.on_task_completed)
        self.task_thread.task_progress.connect(self.update_progress)
        self.task_thread.task_error.connect(self.show_error_dialog)
        self.task_thread.task_hash.connect(self.backup_to_ini)

        self.task_thread2 = TaskThread2()
        self.task_thread2.task_completed.connect(self.on_task_completed)
        self.task_thread2.task_progress.connect(self.update_progress)
        self.task_thread2.task_error.connect(self.show_error_dialog)

        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setMaximum(100)
        self.ui.progressBar.setValue(0)
        self.ui.progressBar.setStyleSheet('QProgressBar {border: 2px solid grey; border-radius: 5px; '
                                          'background-color: #FFFFFF; text-align: center;}'
                                          'QProgressBar::chunk {background: qlineargradient(x1:0, y1:0, x2:1, y2:0,'
                                          'stop:0 #666699, stop:1 #DB7093);}')

        self.ui.addrLineEdit.installEventFilter(self)

        self.ui.actionAbout.triggered.connect(self.show_about_dialog)
        self.ui.actionConfirm.triggered.connect(self.changeToPrevNamen)

        self.ui.plusAction.triggered.connect(lambda: self.setPattern('+'))
        self.ui.minusAction.triggered.connect(lambda: self.setPattern('-'))

    def setPattern(self, signal):
        if signal == '+':
            shared_params.pattern = r'(?<=\+\D*)\d+'
        elif signal == '-':
            shared_params.pattern = r'(?<=\-\D*)\d+'

    def show_about_dialog(self):
        about_dialog = aboutMe()
        about_dialog.exec()

    def eventFilter(self, source, event):
        if event.type() == event.Enter:
            # 鼠标悬浮时显示完整值
            full_value = self.ui.addrLineEdit.text()
            self.ui.addrLineEdit.setToolTip(full_value)
        elif event.type() == event.Leave:
            # 鼠标离开时隐藏提示
            self.ui.addrLineEdit.setToolTip("")
        return super().eventFilter(source, event)

    def chooseDir(self):
        global dirName
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly  # 仅显示文件夹
        dirName = QFileDialog.getExistingDirectory(self, "Select a Folder", "C:/Users", options=options)
        self.ui.addrLineEdit.setText(dirName)

        self.clear_format()

    def clear_format(self):
        # 恢复默认字体和样式
        self.ui.reminderLineEdit.setFont(self.default_font)
        self.ui.reminderLineEdit.setStyleSheet("")
        self.ui.reminderLineEdit.setText(self.default_text)

    def backup_to_ini(self, correspondence):
        # 初始化section计数器
        section = 1

        # 遍历correspondence字典，将对应关系写入ConfigParser对象
        for new_name, old_name in correspondence.items():
            # 使用f字符串构建section的名字
            section_name = f"section{section}"
            config[section_name] = {'new_name': new_name, 'old_name': old_name}
            section += 1

        with open(addrNameChanger + r'prev_names.ini', 'w', encoding='utf-8') as configfile:
            config.write(configfile)

    def changeName(self):
        if shared_params.pattern == "":
            self.show_error_dialog("Please select the separator.")
        else:
            self.task_thread.start()
            self.ui.changePushButton.setEnabled(False)

    def changeToPrevNamen(self):
        self.task_thread2.start()
        self.ui.changePushButton.setEnabled(False)

    def on_task_completed(self):
        self.ui.changePushButton.setEnabled(True)
        self.ui.reminderLineEdit.setText('Congrats! Names have been altered.')
        self.ui.reminderLineEdit.setStyleSheet("QLineEdit { color: blue; font-weight: bold;}")
        os.startfile(dirName)

    def update_progress(self, value):
        self.ui.progressBar.setValue(value)

    def show_error_dialog(self, error_message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")
        msg.setText("An error occurred:")
        msg.setInformativeText(error_message)
        msg.exec_()
        self.ui.changePushButton.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(argv)
    ui = changerUi()

    ui.show()
    exit(app.exec_())
