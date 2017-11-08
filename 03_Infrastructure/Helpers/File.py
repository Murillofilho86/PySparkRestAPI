import os

class File:

    @property
    def fileName(self):
        return self._fileName

    @fileName.setter
    def fileName(self, value):
        self._fileName = value

    @property
    def file(self):
        return self._file

    @file.setter
    def file(self, value):
        self._file = value

    def __init__(self, name):
        self.fileName = name

    def Open(self):
        self.file = open(self.fileName, "a+")

    def Close(self):
        self.file.close()

    def Write(self, text):
        self.file.write(text + "\n")