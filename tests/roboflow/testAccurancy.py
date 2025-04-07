# tests/roboflow/testAccurancy.py

# Imports
from functions import *

# Main
try:
    resp = int(input(strColored(">> Digite qual versão do modelo deseja testar: ", 'white')))

    # Inicializa a comunicação do modelo Roboflow com o Main
    model = initRoboflow(resp)

    folder_Metopolophium = "../../database/Metopolophium"
    folder_Rhopalosiphium = "../../database/Rhopalosiphum padi"
    folder_Schizaphis = "../../database/Schizaphis graminum"
    folder_Sipha = "../../database/Sipha maydis"
    folder_Sitobion = "../../database/Sitobion avenae"

    confidence = {
        "Metopolophium": [],
        "Rhopalosiphum-padi": [],
        "Schizaphis-graminum": [],
        "Sipha-maydis": [],
        "Sitobion-avenae": []
    }

    # Testa a confiança de cada classe do modelo
    testAccuracy(model, folder_Metopolophium, "Metopolophium", confidence)
    testAccuracy(model, folder_Rhopalosiphium, "Rhopalosiphum-padi", confidence)
    testAccuracy(model, folder_Schizaphis, "Schizaphis-graminum", confidence)
    testAccuracy(model, folder_Sipha, "Sipha-maydis", confidence)
    testAccuracy(model, folder_Sitobion, "Sitobion-avenae", confidence)

    print(confidence)

    # Calcula e exibe a média de confiança para cada classe
    print(strColored(f"\n>> Precisão do modelo {resp} para as classes", 'white'))
    print(perAccuracy("Metopolophium", confidence))
    print(perAccuracy("Rhopalosiphum-padi", confidence))
    print(perAccuracy("Schizaphis-graminum", confidence))
    print(perAccuracy("Sipha-maydis", confidence))
    print(perAccuracy("Sitobion-avenae", confidence))

except:
    print(strColored(">> ERRO: Versão não existente do modelo Roboflow", 'red'))
    exit(0)
