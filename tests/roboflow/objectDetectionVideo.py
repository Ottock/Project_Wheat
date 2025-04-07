# tests/roboflow/objectDetectionVideo.py

# Problemas: Vídeo extremamente lento pela função apneas funcionar com
# imagens, mas a previsão funciona :)

# Imports
import cv2

from functions import initRoboflow

# Roboflow client API key
# rf = Roboflow(api_key="1l0qBJJkbebPGJ18Hutv")

# Acessa o projeto, workspace e sua versão
#project_name = "projeto-ic-gcsp"
# project = rf.workspace(project_name).project("pragas-ic-gcsp-m8j84")
# version = project.version(1)
# model = version.model

# Câmera a ser acessada (WebCam)
cap = cv2.VideoCapture(0)

model = initRoboflow(2)

# Verifica se a Câmera pode ser acessada
if not cap.isOpened():
    print(">> Erro ao abrir a câmera")
else:
    while True:
        # Read frame by frame of the camera
        ret, frame = cap.read()

        if not ret:
            print(">> Erro ao capturar o frame")
            break

        # Previsões do modelo
        response = model.predict(frame, confidence=40, overlap=30).json()
        predictions = response['predictions']

        # Desenha caixas identificadoras no frame
        for pred in predictions:
            # Previsões veitas pelo modelo
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

            # Desenha a caixa                          (B,   G,   R)
            # cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 252, 255), 2)
            match label:
                case "Metopolophium":
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 252, 199), 2)
                case "Rhopalosiphum-padi":
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 34, 134), 2)
                case "Schizaphis-graminum":
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (86, 0, 254), 2)
                case "Sipha-maydis":
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (206, 255, 0), 2)
                case "Sitobion avenae":
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 128, 255), 2)

            # Escrever o rótulo da classe e a confiança
            text = f"{label}: [{confidence:.2f}]"
            cv2.putText(frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

        # Exibe o frame com as caixas identificadoras
        cv2.imshow('Detecções', frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Fechamento
    cap.release()
    cv2.destroyAllWindows()
