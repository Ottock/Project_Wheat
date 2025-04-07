# functions/__init__.py

# Imports
import os
import cv2
import smtplib
from auth import API, WORKSPACE, PROJECT

from roboflow import Roboflow
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# Functions
def initRoboflow(version):
    """
    initRoboflow(version): Função que inicializa o Roboflow dentro do programa.

    :param version: Versão do modelo Roboflow a ser utilizada.
    :return: Modelo associado à versão do parâmetro, se a versão for válida. Caso contrário, None.
    """
    try:
        # Inicializa o cliente Roboflow
        rf = Roboflow(API)

        # Acessa o projeto e workspace
        workspace = rf.workspace(WORKSPACE)
        project = workspace.project(PROJECT)

        # Acessa a versão do modelo
        model_version = project.version(version)

        print(strColored(">> Conexão com modelo Roboflow sucedida", 'green'))
        return model_version.model

    except ValueError as e:
        print(strColored(f">> ERRO: {str(e)}. Verifique a versão do modelo.", 'red'))
        return None
    except Exception as e:
        print(strColored(f">> ERRO: {str(e)}. Verifique as credenciais e configuração do projeto.", 'red'))
        return None

def testAccuracy(version_model, folder_path, clas, confidence_dict):
    """
    testAccuracy(version_model, folder_path, clas, confidence_dict): Função que realiza um teste de confiança da classe do modelo Roboflow.

    :param version_model: Versão do modelo Roboflow a ser utilizada.
    :param folder_path: Caminho da pasta que contém as imagens a serem testadas pelo modelo Roboflow.
    :param clas: Classe do objeto a ser utilizada para a predição.
    :param confidence_dict: Dicionário onde a precisão do modelo Roboflow será armazenada.
    :return: None.
    """

    # Objeto a ser utilizado para a análise
    model = version_model

    # Busca dentro da pasta as imagens a serem analisadas
    for filename in os.listdir(folder_path):
        if filename.endswith((".png", ".jpg")):
            image_path = os.path.join(folder_path, filename)
            image = cv2.imread(image_path)

            if image is None:
                print(strColored(f">> Erro ao carregar a imagem em: {image_path}", 'red'))
            else:
                # Início da análise do modelo
                try:
                    response = model.predict(image_path, confidence=50, overlap=30).json()
                    predictions = response['predictions']

                    for pred in predictions:
                        pred_class = pred['class']
                        if pred_class == clas:
                            confidence_dict[pred_class].append(pred['confidence'])
                            print(confidence_dict)
                except Exception as e:
                    print(strColored(f">> ERRO: Falha na predição da imagem {filename}: {str(e)}", 'red'))


def perAccuracy(clas, confidence_dict):
    """
    perAccuracy(clas, confidence_dict): Função que realiza o cálculo da média de confiança de uma dada classe de objeto do modelo Roboflow.

    :param clas: Nome da classe de objeto a ser utilizada.
    :param confidence_dict: Dicionário que armazena a confiança de várias imagens, que será utilizado para o cálculo.
    :return: String que contém a média de confiança da classe do modelo Roboflow, formatada com a cor correspondente.
    """

    confidences = confidence_dict.get(clas, [])
    if confidences:
        media_conf = sum(confidences) / len(confidences)
    else:
        media_conf = 0

    # String com cores
    if media_conf <= 0.20:
        return strColored(f">> {clas}: {media_conf:.2f}", 'dark_red')
    elif 0.20 < media_conf <= 0.30:
        return strColored(f">> {clas}: {media_conf:.2f}", 'red')
    elif 0.30 < media_conf <= 0.40:
        return strColored(f">> {clas}: {media_conf:.2f}", 'dark_orange')
    elif 0.40 < media_conf <= 0.50:
        return strColored(f">> {clas}: {media_conf:.2f}", 'orange')
    elif 0.50 < media_conf <= 0.60:
        return strColored(f">> {clas}: {media_conf:.2f}", 'dark_yellow')
    elif 0.60 < media_conf <= 0.70:
        return strColored(f">> {clas}: {media_conf:.2f}", 'yellow')
    elif 0.70 < media_conf <= 0.80:
        return strColored(f">> {clas}: {media_conf:.2f}", 'dark_green')
    else:
        return strColored(f">> {clas}: {media_conf:.2f}", 'cyan')


def captureImage(frame, imageName="capturedImage.jpg"):
    """
    captureImage(frame, imageName="capturedImage.jpg"): Função que captura um frame e o armazena com um nome especifico.

    :param frame: frame a ser capturado.
    :param imageName: nome do frame a ser capturado.
    :return: caminho armazenado.
    """

    cv2.imwrite(imageName, frame)
    print(strColored(f">> Imagem salva em: {imageName}", 'blue'))

    return imageName

def sendEmail(email_receiver, email_subject, email_body, image_path=None):
    """
    sendEmail(email_receiver, email_subject, email_body, image_path): Função que envia um e-mail utilizando o servidor SMTP do Gmail.

    :param email_receiver: Endereço de e-mail do destinatário.
    :param email_subject: Assunto do e-mail.
    :param email_body: Corpo do e-mail.
    :param image_path: Caminho para a imagem a ser anexada (opcional).
    :return: None.
    """

    # Informações do E-mail do emissor e senha da conta
    # email: "projectwheat50@gmail.com"
    # password: Project1234
    email_sender = "projectwheat50@gmail.com"
    email_password = "uevv bake eqvr psbq"

    # Verifica se o email do destinatário está vazio
    if not email_receiver:
        print(strColored(">> ERRO: O endereço de e-mail do destinatário não pode estar vazio", 'red'))
        return

    # Construindo a mensagem
    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = email_subject

    # Corpo do e-mail
    msg.attach(MIMEText(email_body, 'plain'))

    # Anexando a imagem, se fornecida
    if image_path:
        try:
            with open(image_path, 'rb') as img_file:
                img = MIMEImage(img_file.read())
                img.add_header('Content-ID', '<imagem1>')
                img.add_header('Content-Disposition', 'inline', filename='PragasDetectadas.jpg')
                msg.attach(img)
        except Exception as e:
            print(strColored(f">> ERRO: Falha ao anexar a imagem: {str(e)}", 'red'))
            return

    # Conexão com SMTP Server
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_sender, email_password)
        text = msg.as_string()
        server.sendmail(email_sender, email_receiver, text)
        server.quit()
        print(strColored(">> E-mail enviado com sucesso", 'green'))
    except Exception as e:
        print(strColored(f">> ERRO: Falha ao enviar o e-mail: {str(e)}", 'red'))


def strColored(text, color):
    """
    strColored(text, color): Função que aplica cor ao texto para exibição no terminal.

    :param text: Texto a ser colorido.
    :param color: Cor a ser aplicada ao texto. As cores disponíveis da função são:
                  'red', 'dark_red', 'orange', 'dark_orange', 'green', 'dark_green', 'yellow',
                  'dark_yellow', 'light_purple', 'purple', 'cyan', 'light_gray', 'gray', 'blue', 'white'.
    :return: String Texto colorido como string formatada.
    """

    colors = {
        'red': "\033[91m{}\033[00m",
        'dark_red': "\033[31m{}\033[00m",
        'orange': "\033[38;5;208m{}\033[00m",
        'dark_orange': "\033[38;5;202m{}\033[00m",
        'green': "\033[92m{}\033[00m",
        'dark_green': "\033[32m{}\033[00m",
        'yellow': "\033[93m{}\033[00m",
        'dark_yellow': "\033[33m{}\033[00m",
        'light_purple': "\033[94m{}\033[00m",
        'purple': "\033[95m{}\033[00m",
        'cyan': "\033[96m{}\33[00m",
        'light_gray': "\033[97m{}\033[00m",
        'gray': "\033[90m{}\033[00m",
        'blue': "\033[94m{}\033[00m",
        'white': "\033[97m{}\033[00m",
    }
    return colors.get(color, 'white').format(text)
