import os
import sys
sys.path.insert(
    0, 
    os.path.abspath(".."))

import config
import datetime
from Helpers.File import File

class Log:

    def Add(fileName, text):
        arquivo = File(config.LOG_PATH + fileName)
        arquivo.Open()
        arquivo.Write(str(datetime.datetime.now()) + ": " + text)
        arquivo.Close()