# tests/roboflow/modelDownload/py

# Imports
from roboflow import Roboflow
import functions

# Roboflow Model
# API Key
api_key = "8UjXP8kvalxT275T5XgN"
workspace_name = "projeto-ic"
project_name = "ic-pragas"
rf = Roboflow(api_key)

# Project Acess
project = rf.workspace(workspace_name).project(project_name)
resp = int(input(functions.strColored(">> Digite qual versão do modelo deseja baixar: ", 'blue')))

try:
    version = project.version(resp)
    # Dataset
    dataset = version.download("yolov5")
except:
    print(functions.strColored(">> ERRO: Versão não existente do modelo Roboflow", 'red'))
    exit(0)
