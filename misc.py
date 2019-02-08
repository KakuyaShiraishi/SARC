from struct import *
import os

class ReadStringUntilNull(object):
    def __init__(stringFromFile):
        stringTempOutput = b''
        stringBuffer = unpack('<1s', stringFromFile.read(1))[0]
        stringTempOutput += stringBuffer
        while stringBuffer != b'\x00':
            stringBuffer = unpack('<1s', stringFromFile.read(1))[0]
            if stringBuffer != b'\x00':
                stringTempOutput += stringBuffer
            else:
                pass
            stringOutput = stringTempOutput.decode("utf-8")
        return stringOutput

class Writefile:
    def __init__(self, newName, newData):
        NewFile = open(newName, mode='bw', buffering=0)
        NewFile.write(newData)
        NewFile.close()

class CreateDirOnlyIfNoneExist(object):
    def __init__(self, pathInput):
        try:
            os.mkdir(os.path.join(pathInput))
        except FileExistsError:
            pass
