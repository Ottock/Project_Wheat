# src/mainImage.py

# Imports
import cv2
import time
import matplotlib.pyplot as plt

from functions import initRoboflow, strColored, sendEmail

# Main
try:
    resp = int(input(strColored(">> Digite qual versão do modelo deseja testar: ", 'white')))

    # Inicializa a comunicação do modelo Roboflow com o Main
    model = initRoboflow(resp)
except:
    print(strColored("\n>> ERRO: Versão não existente do modelo Roboflow", 'red'))
    exit(0)

# Path da imagem para ser testada pelo modelo
image_path = "database/Metopolophium/18.jpg"
#image_path = "src/database/Rhopalosiphum padi/11.jpg"
#image_path = "database/Schizaphis graminum/18.jpg"
#image_path = "src/database/Sipha maydis/7.jpg"
#image_path = "database/Sitobion avenae/3.jpg"

#image_path = "../database/teste.png"
image = cv2.imread(image_path)

# Testa se a imagem pode ser acessada
if image is None:
    print(strColored(f">> ERRO: Não foi possível carregar a imagem em: {image_path}", 'red'))
else:
    try:
        # Previsões feitas pelo modelo
        response = model.predict(image_path, confidence=50, overlap=30).json()
        predictions = response['predictions']

        # Extrai informações das previsões do modelo
        Metopolophium = 0
        RhopalosiphumPadi = 0
        SchizaphisGraminum = 0
        SiphaMaydis = 0
        SitobionAvenae = 0

        # Modelo não identifica nenhuma presença de pragas
        if not predictions:
            print(strColored(">> Nenhuma praga foi identificada", 'yellow'))
            exit()

        # Pragas identificadas
        for pred in predictions:
            print(predictions)
            x = int(pred['x'])
            y = int(pred['y'])
            width = int(pred['width'])
            height = int(pred['height'])
            label = pred['class']
            confidence = pred['confidence']

            # Coordenadas
            x1 = x - width // 2
            y1 = y - height // 2
            x2 = x + width // 2
            y2 = y + height // 2

            # Desenha a caixa com a cor correspondente à praga identificada
            match label:
                case "Metopolophium":
                    Metopolophium += 1
                    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 252, 199), 2)
                case "Rhopalosiphum-padi":
                    RhopalosiphumPadi += 1
                    cv2.rectangle(image, (x1, y1), (x2, y2), (255, 34, 134), 2)
                case "Schizaphis-graminum":
                    SchizaphisGraminum += 1
                    cv2.rectangle(image, (x1, y1), (x2, y2), (86, 0, 254), 2)
                case "Sipha-maydis":
                    SiphaMaydis += 1
                    cv2.rectangle(image, (x1, y1), (x2, y2), (206, 255, 0), 2)
                case "Sitobion-avenae":
                    SitobionAvenae += 1
                    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 128, 255), 2)

            # Desenha um retângulo de uma cor (B, G, R) com as coordenadas da previsão
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

            # Insere a classe do objeto e a confiança que o modelo tem do objeto
            text = f"{label}: [{confidence:.2f}]"
            cv2.putText(image, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

        # Resultados
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        plt.imshow(image_rgb)
        plt.axis('off')
        plt.show()
        currentTime = time.time()

        # Salva a imagem no formato BGR (correta para OpenCV)
        cv2.imwrite("PragaDetectada.jpg", image)

        # Envia o e-mail com a imagem anexada
        sendEmail(
            "", # e-mail que vai receber
            "Pragas Identificadas",
            f">> {time.ctime(currentTime)}\n" +
            f"\nPragas identificadas: \n" +
            f"\nPulgão-das-folhas (Metopolophium dirhodum): {Metopolophium}" +
            f"\nPiolho-da-cereja-brava (Rhopalosiphum padi): {RhopalosiphumPadi}" +
            f"\nPulgão-verde-dos-cereais (Schizaphis graminum): {SchizaphisGraminum}" +
            f"\nPulgão-preto-dos-cereais (Sipha maydis): {SiphaMaydis}" +
            f"\nPulgão-da-espiga (Sitobion avenae): {SitobionAvenae}",
            "PragaDetectada.jpg"
        )

    except Exception as e:
        print(strColored(f">> ERRO: {str(e)}", 'red'))
