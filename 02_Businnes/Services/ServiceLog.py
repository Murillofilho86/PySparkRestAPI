import os
import sys
sys.path.insert(
    0, 
    os.path.abspath(os.path.join(os.path.dirname(os.path.abspath('../03_Infrastructure/Helpers/') + "\\"), '..')))

from Helpers.Log import Log

class ServiceLog:

    def Add(fileName, text):
        Log.Add(fileName, text)