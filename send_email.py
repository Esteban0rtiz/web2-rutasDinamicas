uaimport smtplib
from email.mime.text import MIMEText

def send_email(subject, body, to_email):
    # Configura los detalles de la cuenta de correo
    from_email = "ecuaplush20244@gmail.com"  # Reemplaza con tu dirección de correo electrónico
    password = "plus2021"          # Reemplaza con tu contraseña

    # Crea el mensaje de correo
    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = from_email
    message["To"] = to_email

    # Conéctate al servidor SMTP y envía el correo
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, message.as_string())

# Ejemplo de uso
send_email("Prueba de Jenkins", "Este es un correo de prueba con script python.", "ecuaplush010@gmail.com")
