import smtplib
from email.message import EmailMessage
import mimetypes
import os


def enviar_email(dir_raiz):
    smtpsrv = "smtp.office365.com"
    smtpserver = smtplib.SMTP(smtpsrv, 587)

    msg = EmailMessage()

    # textos do email
    assunto = 'MENSAGEM AUTOMÁTICA -> Log Limpeza do Unico Contabil'
    body = open(dir_raiz + os.sep + 'corpo_email.txt',
                'r', encoding='utf-8').read()

    msg['Subject'] = assunto
    msg['From'] = 'diogo.rodrigues@supervisao.com.vc'
    msg['To'] = ('diogoheck6@gmail.com', 'diogo.rodrigues@supervisao.com.vc')

    # estruturação de um arquivo anexo
    anexo_path = dir_raiz + os.sep + 'log_limpeza_u_dp.txt'
    anexo_arquivo = os.path.basename(anexo_path)
    mime_type, _ = mimetypes.guess_type(anexo_path)
    mime_type, mime_subtype = mime_type.split('/', 1)

    msg.set_content(body)

    # adiciona o arquivo anexo ao email
    with open(anexo_path, 'rb') as ap:
        msg.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype,
                           filename=os.path.basename(anexo_path))

    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.login('diogo.rodrigues@supervisao.com.vc', 'D@241708')
    smtpserver.send_message(msg)
    smtpserver.close()


if __name__ == '__main__':
    enviar_email()
