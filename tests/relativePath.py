# tests/RelativePath.py

# Imports
import os
import cv2
import matplotlib.pyplot as plt

# Path da imagem para ser testada pelo modelo
image_path = "database/Sipha maydis/1.jpg"
image = cv2.imread(image_path)

# Testa se a imagem pode ser acessada
if image is None:
    print(f">> ERRO: Falha em carregar imagem em: {image_path}")
else:
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.axis('off')
    plt.show()
