import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, to_email):
    from_email = "tu_correo@gmail.com"  # Reemplaza con tu dirección de correo electrónico
    password = "tu_contraseña"          # Reemplaza con tu contraseña

    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = from_email
    message["To"] = to_email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, message.as_string())

# Ejemplo de uso
send_email("Prueba de Jenkins", "Este es un correo de prueba enviado desde Jenkins.", "destinatario@example.com")
