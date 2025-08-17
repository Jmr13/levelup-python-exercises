import smtplib

SENDER_EMAIL = ""
SENDER_PASSWORD = ""

def send_email(receiver_email, subject, body):
    message = f"Subject: {subject} \n\n {body}"
    with smtplib.SMTP("smtp.office365.com", 587) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, message)