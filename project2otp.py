import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

def otp(to_email):
    otp = random.randint(1111,9999)

    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    username = "ashokmangali631@gmail.com"
    password = "injq lofl pivt cddh"

    from_email = "ashokmangali631@gmail.com"
    subject = "OTP for verification"
    body = f"The OTP for Verification is {otp}"

    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body,"plain"))

    server = smtplib.SMTP(smtp_server,smtp_port)
    server.starttls()
    server.login(username,password)
    server.send_message(msg)
    server.quit()
    print("Email sent !")

    votp = int(input("Enter Otp: "))
    if votp == otp:
        print("Verification Success")
    else:
        print("Verification Failed")
otp("ashokmangali631@gmail.com")
    
    
