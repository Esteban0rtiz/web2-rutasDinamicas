import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, to_email):
    from_email = "ecuaplush20244@gmail.com"
    app_password = "zpbk hakh swel ehyg"  # Reemplaza con tu contraseña de aplicación

    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = from_email
    message["To"] = to_email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(from_email, app_password)
            server.sendmail(from_email, to_email, message.as_string())
        print("Correo enviado con éxito.")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

# Ejemplo de uso
send_email("Prueba de Jenkins", "Este es un correo de prueba con script python.", "ecuaplush010@gmail.com")
