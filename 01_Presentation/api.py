import os
import sys
sys.path.insert(
    0, 
    os.path.abspath(
        os.path.join(os.path.dirname(os.path.abspath('../02_Businnes/Services/') + "\\"), '..')))

import json
from Services.ServiceApi import ServiceApi
from flask import Flask, request
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/Start", methods = ["GET"])
def Start():
    if request.method == "GET":
        servico = ServiceApi()
        return servico.Start()

@app.route("/Load", methods = ["POST"])
def Load():
    if request.method == "POST":
        servico = ServiceApi()
        parameters = request.form
        token = parameters["token"]
        urlData = parameters["urlData"]
        type = parameters["type"]
        return servico.Load(token, urlData, type)

app.run()