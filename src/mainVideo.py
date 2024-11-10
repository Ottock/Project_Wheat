# src/mainVideo.py

# Imports
import cv2
import time
from functions import initRoboflow, strColored, sendEmail, captureImage

# Main
try:
    resp = int(input(strColored(">> Digite qual versão do modelo deseja testar: ", 'white')))

    # Inicializa a comunicação do modelo Roboflow com o Main
    model = initRoboflow(resp)
except Exception as e:
    print(strColored(f"\n>> ERRO: {e}", 'red'))
    exit(0)

# Inicializa a webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print(strColored(">> ERRO: Não foi possível acessar a webcam", 'red'))
    exit(0)

# Variáveis de controle de tempo
last_capture_time = time.time()
time_seconds = 10

while True:
    ret, frame = cap.read()

    if not ret:
        print(strColored(">> ERRO: Não foi possível capturar o quadro da webcam", 'red'))
        break

    # Mostrar o vídeo capturado ao vivo
    cv2.imshow("Project Wheat 6.0", frame)

    # Captura de imagem a cada intervalo definido
    if time.time() - last_capture_time >= time_seconds:
        last_capture_time = time.time()

        # Realiza a previsão no frame capturado
        try:
            response = model.predict(frame, confidence=50, overlap=30).json()
            predictions = response['predictions']

            # Variáveis para armazenar o número de pragas identificadas
            Metopolophium = 0
            RhopalosiphumPadi = 0
            SchizaphisGraminum = 0
            SiphaMaydis = 0
            SitobionAvenae = 0

            # Modelo não identifica nenhuma presença de pragas
            if not predictions:
                print(strColored(f">> Nenhuma praga foi identificada: {time.ctime(time.time())}", 'yellow'))
            else:
                print(strColored(f">> Praga identificada: {time.ctime(time.time())}", 'green'))

                # Pragas identificadas
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

                    # Desenha a caixa com a cor correspondente à praga identificada
                    match label:
                        case "Metopolophium":
                            Metopolophium += 1
                            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 252, 199), 2)
                        case "Rhopalosiphum-padi":
                            RhopalosiphumPadi += 1
                            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 34, 134), 2)
                        case "Schizaphis-graminum":
                            SchizaphisGraminum += 1
                            cv2.rectangle(frame, (x1, y1), (x2, y2), (86, 0, 254), 2)
                        case "Sipha-maydis":
                            SiphaMaydis += 1
                            cv2.rectangle(frame, (x1, y1), (x2, y2), (206, 255, 0), 2)
                        case "Sitobion-avenae":
                            SitobionAvenae += 1
                            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 128, 255), 2)

                    # Insere a classe do objeto e a confiança que o modelo tem do objeto
                    text = f"{label}: [{confidence:.2f}]"
                    cv2.putText(frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

                # Exibe a imagem com as anotações para verificação
                cv2.imshow("Project Wheat 6.0 - Detection", frame)

                # Salva a imagem capturada
                image_path = captureImage(frame, "PragaDetectada.jpg")

                # Envia o e-mail com a foto
                try:
                    sendEmail(
                        "", # e-mail que vai receber
                        "Pragas Identificadas",
                        f""">> {time.ctime(time.time())}\n
                                  \nPragas identificadas: \n
                                  Pulgão-das-folhas (Metopolophium dirhodum): {Metopolophium}
                                  Piolho-da-cereja-brava (Rhopalosiphum padi): {RhopalosiphumPadi}
                                  Pulgão-verde-dos-cereais (Schizaphis graminum): {SchizaphisGraminum}
                                  Pulgão-preto-dos-cereais (Sipha maydis): {SiphaMaydis}
                                  Pulgão-da-espiga (Sitobion avenae): {SitobionAvenae}
                                  """,
                                  image_path
                    )

                except Exception as e:
                    print(strColored(f">> ERRO ao enviar email: {e}", 'red'))

        except Exception as e:
            print(strColored(f">> ERRO: {e}", 'red'))

    # Fecha a janela ao pressionar 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a câmera e fecha as janelas
cap.release()
cv2.destroyAllWindows()
