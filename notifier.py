import smtplib
from email.message import EmailMessage
import os

class EmailNotifier:
    def __init__(self):
        self.sender = os.getenv("EMAIL_SENDER")
        self.password = os.getenv("EMAIL_PASSWORD")
        self.receiver = os.getenv("EMAIL_RECEIVER")

    def send_alert(self, subject, body):
        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject'] = subject
        msg['From'] = self.sender
        msg['To'] = self.receiver

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(self.sender, self.password)
                smtp.send_message(msg)
            print(" Alert sent successfully!")
        except Exception as e:
            print(f" Failed to send email: {e}")