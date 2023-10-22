from os import path, makedirs


def nameChangerPathDef():
    rootPath = path.expanduser('~')
    try:
        makedirs(rootPath + r'\nameChanger')
        addrNameChanger = rootPath + r'\nameChanger'
    except:
        addrNameChanger = rootPath + r'\nameChanger'

    return addrNameChanger