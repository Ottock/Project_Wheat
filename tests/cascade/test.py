# tests/cascade/test.py

# Imports
import cv2

# Carregar o classificador Haar Cascade
cascade_path = 'cascade.xml'
pestClassif = cv2.CascadeClassifier(cascade_path)

if pestClassif.empty():
    print(f'Erro ao carregar o classificador em {cascade_path}')
    exit()

# Carregar uma imagem de teste
image_path = r"1.jpg"
image = cv2.imread(image_path)

if image is None:
    print(f'Erro ao carregar a imagem em {image_path}')
    exit()

# Converter a imagem para escala de cinza
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detectar objetos usando o classificador Haar Cascade
pests = pestClassif.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(70, 78))

if len(pests) == 0:
    print('Nenhuma praga detectada')
else:
    # Desenhar retângulos e rotular objetos detectados em vermelho
    for (x, y, w, h) in pests:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)  # cor vermelha
        cv2.putText(image, 'Praga', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_AA)  # cor vermelha

    # Exibir a imagem com os objetos detectados
    cv2.imshow('Detecção em Imagem', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
