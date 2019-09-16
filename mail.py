'''
Program to send mail from GMAIL using SMTP
'''
import smtplib

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
GMAIL_USERNAME = 'username@gmail.com'
GMAIL_PASSWORD = 'xxxxxxx' #CAUTION: This is stored in plain text!

recipient = 'someone@example.com'
subject = 'Test'
emailText = 'This is the content of the e-mail.'

emailText = "" + emailText + ""

headers = ["From: " + GMAIL_USERNAME,
           "Subject: " + subject,
           "To: " + recipient,
           "MIME-Version: 1.0",
           "Content-Type: text/html"]
headers = "\r\n".join(headers)

session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

session.ehlo()
session.starttls()
session.ehlo

session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + emailText)
session.quit()

