import ssl
import smtplib
from email.message import EmailMessage

remitente = 'dirección-del-remitente'
contraseña = 'contraseña-del-remitente'
destinatario = 'dirección-del-destinatario'

asunto = 'Test'
cuerpo = """
Este mail ha sido enviado desde Python!
"""

# Crear objeto de mail
em = EmailMessage()
em['From'] = remitente
em['To'] = destinatario
em['Subject'] = asunto
em.set_content(cuerpo)

# Añadir SSL (extra de seguridad)
context = ssl.create_default_context()

# Iniciar sesión y enviar el mail
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(remitente, contraseña)
    smtp.sendmail(remitente, destinatario, em.as_string())