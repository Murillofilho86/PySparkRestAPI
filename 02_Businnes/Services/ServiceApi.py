import os
import sys
sys.path.insert(
    0, 
    os.path.abspath(
        os.path.join(os.path.dirname(os.path.abspath('../03_Infrastructure/DAO/') + "\\"), '..')))

sys.path.insert(
    0, 
    os.path.abspath(
        os.path.join(os.path.dirname(os.path.abspath('../02_Businnes/Services/') + "\\"), '..')))

import json
from DAO.ProcessDAO import ProcessDAO
from Services.ServiceLog import ServiceLog
from Services.ServiceToken import ServiceToken

class ServiceApi:

    @property
    def Errors(self):
        return self._Errors

    @Errors.setter
    def Errors(self, value):
        self._Errors = value

    def __init__(self):
        self.Errors = []

    def Start(self):
        token = str(ServiceToken.Create())
        ProcessDAO.Add(1, token, token)
        ServiceLog.Add(token, token)
        return json.dumps({"Token": token, "Errors": self.Errors})

    def Load(self, token, urlData, type):
        if not self.HaveValidParamaters(token, urlData, type):
            return json.dumps({"Errors": self.Errors})
        else:
            data = self.BuildDataForLoad(token, urlData, type)
            ProcessDAO.Add(2, token, json.dumps(data))
            ServiceLog.Add(token, json.dumps(data))
            return json.dumps({"Errors": self.Errors})

    def HaveValidParamaters(self, token, urlData, type):
        return self.ParametersHaveValues(token, urlData, type) \
                and self.IsValidType(type)

    def ParametersHaveValues(self, token, urlData, type):
        haveValues =  token != None \
                and len(token) > 0 \
                and urlData != None \
                and len(urlData) > 0 \
                and type != None \
                and len(type) > 0
        if not haveValues:
            self.Errors.append("Null parameters")
        return haveValues

    def IsValidType(self, type):
        if type == "CSV":
            self.Errors.append("Invalid type: valid is only CSV")
            return False
        return True

    def BuildDataForLoad(self, token, urlData, type):
        return {"token": token, "urlData": urlData, "type": type}
