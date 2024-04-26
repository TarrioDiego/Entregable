import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, subject, body):
    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Attach the body to the email
    message.attach(MIMEText(body, 'plain'))

    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com',587) # Use the SMTP server of your email provider
    session.starttls() # Enable TLS
    session.login(sender_email, sender_password)

    # Send the email
    text = message.as_string()
    session.sendmail(sender_email, receiver_email, text)
    session.quit()
    print("Mail Sent")