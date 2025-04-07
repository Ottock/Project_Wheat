# tests/EmailSender.py

# Imports
from functions import strColored
from functions import sendEmail

# Main
email = input(strColored(">> Insira o E-mail do remetente: ", 'white'))
assunto = input(strColored(">> Digite o assunto do E-mail: ", 'white'))
corpo = input(strColored(">> Digite o corpo do E-mail: ", 'white'))

sendEmail(email, assunto, corpo)
