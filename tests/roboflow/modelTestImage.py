# tests/roboflow/modelTestImage.py

# Imports
import cv2
import matplotlib.pyplot as plt

from functions import initRoboflow

# Roboflow client API key
# rf = Roboflow(api_key="1l0qBJJkbebPGJ18Hutv")

# Acessa o projeto, workspace e sua versão
#project_name = "projeto-ic-gcsp"
# project = rf.workspace(project_name).project("pragas-ic-gcsp-m8j84")
# version = project.version(1)
# model = version.model

# Path da imagem para ser testada pelo modelo
image_path = "../../src/database/Schizaphis graminum/27.jpg"
image = cv2.imread(image_path)

model = initRoboflow(2)

# Testa se a imagem pode ser acessada
if image is None:
    print(f">> ERRO: Falha ao carregar a imagem em: {image_path}")
else:
    # Previsoes do modelo
    response = model.predict(image_path, confidence=40, overlap=30).json()
    predictions = response['predictions']

    # Previsões feitas pelo modelo
    print(predictions)

    # Extrai informações das previsões do modelo
    for pred in predictions:
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

        # Desenha um retangulo de uma cor (B, G, R) com as coordenadas da previsao
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

        # Insere a classe do objeto e a confianca que o modelo tem do objeto
        text = f"{label}: [{confidence:.2f}]"
        cv2.putText(image, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

    # Resultados
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.axis('off')
    plt.show()
