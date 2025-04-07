# tests/roboflow/modelTestVideo.py

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

# Câmera a ser acessada
cap = cv2.VideoCapture(0)

# Inicialização do Roboflow e a versão do modelo
model = initRoboflow(1)

# Verifica se a Camera pode ser acessada
if not cap.isOpened():
    print(">> Erro ao abrir a câmera")
else:
    while True:
        # Le frame por frame a camera
        ret, frame = cap.read()

        if not ret:
            print(">> Erro ao capturar o frame")
            break

        # Salva o frame atual em uma imagem
        temp_image_path = "temp_frame.jpg"
        cv2.imwrite(temp_image_path, frame)

        # Previsões do modelo
        response = model.predict(temp_image_path, confidence=40, overlap=30).json()
        predictions = response['predictions']

        # Extrai informações das previsões do modelo
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
            # Draw box on the image
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

            # Escrever o rótulo da classe e a confiança
            text = f"{label}: [{confidence:.2f}]"
            cv2.putText(frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

        # Exibe o frame com as caixas identificadoras
        cv2.imshow("Detecções YOLOv5", frame)

        # Pressionar 'q' para encerrar a camera
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Fechamento
    cap.release()
    cv2.destroyAllWindows()
