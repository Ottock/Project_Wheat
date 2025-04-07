# Imports
import os
from functions import strColored, initRoboflow, perAccuracy

# Main
try:
    # Inicializa a comunicação do modelo Roboflow
    resp = int(input(strColored(">> Digite qual versão do modelo deseja testar: ", 'white')))
    model = initRoboflow(resp)
    if model is None:
        print(strColored(">> ERRO: Não foi possível inicializar o modelo Roboflow", 'red'))
        exit(0)

    # Sub-Pastas do database das imagens das pragas
    folder_Metopolophium = r"database/Metopolophium"
    folder_Rhopalosiphium = r"database/Rhopalosiphum padi"
    folder_Schizaphis = r"database/Schizaphis graminum"
    folder_Sipha = r"database/Sipha maydis"
    folder_Sitobion = r"database/Sitobion avenae"

    confidence = {
        "Metopolophium": [],
        "Rhopalosiphum-padi": [],
        "Schizaphis-graminum": [],
        "Sipha-maydis": [],
        "Sitobion-avenae": []
    }


    # Função para calcular a precisão do modelo para uma pasta específica
    def testAccuracy(model, folder_path, class_name, confidence_dict):
        for image_name in os.listdir(folder_path):
            image_path = os.path.join(folder_path, image_name)
            result = model.predict(image_path).json()
            predictions = result['predictions']

            # Obtém a classe prevista com a maior confiança
            if predictions:
                print(predictions)
                top_prediction = max(predictions, key=lambda x: x['confidence'])
                predicted_class = top_prediction['class']
                confidence_score = top_prediction['confidence']

                if predicted_class == class_name:
                    confidence_dict[class_name].append(confidence_score)


    # Testa a confiança de cada classe do modelo
    testAccuracy(model, folder_Metopolophium, "Metopolophium", confidence)
    testAccuracy(model, folder_Rhopalosiphium, "Rhopalosiphum-padi", confidence)
    testAccuracy(model, folder_Schizaphis, "Schizaphis-graminum", confidence)
    testAccuracy(model, folder_Sipha, "Sipha-maydis", confidence)
    testAccuracy(model, folder_Sitobion, "Sitobion-avenae", confidence)

    # Calcula e exibe a média de confiança para cada classe
    print(strColored(f"\n>> Precisão do modelo {resp} para cada classe", 'white'))
    print(perAccuracy("Metopolophium", confidence))
    print(perAccuracy("Rhopalosiphum-padi", confidence))
    print(perAccuracy("Schizaphis-graminum", confidence))
    print(perAccuracy("Sipha-maydis", confidence))
    print(perAccuracy("Sitobion-avenae", confidence))

except ValueError:
    print(strColored(">> ERRO: Valor digitado não é um número inteiro válido", 'red'))
except Exception as e:
    print(strColored(f">> ERRO: {str(e)}", 'red'))
