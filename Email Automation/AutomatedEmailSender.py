import smtplib
from email.message import EmailMessage

#-------------------------------------------------------
# Function:  Marvellous_send_mail
# Description:  Sends email using Gmail SMTP Server
#--------------------------------------------------------

def send_mail(sender, app_password, reciever, subject, body):

    #Step1: Create Email Object
    msg = EmailMessage()

    #Step2: Set mail headers
    msg["From"] = sender
    msg["To"] = reciever
    msg["Subject"] = subject

    #Step3: Add mail body
    msg.set_content(body)

    #Step4: Create SMTP SSL connection manually
    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    #Step5: Login using gmail +  app password
    smtp.login(sender, app_password)

    #Step6: Send the mail
    smtp.send_message(msg)

    #Step7: Close connection manually
    smtp.quit()

#-----------------------------------------
# Function:  main
# Description:  Driver code
#-----------------------------------------

def main():

    #Always use separate temporary/testing account
    sender_mail = "automationforpython0@gmail.com"

    # App Password generated from Google Account
    app_password = "yejs gqeq ryds dstx"

    # Your Second Email for testing
    reciever_email = "photos2of2025@gmail.com"

    subject = "Test Mail from Python Script"

    subject = "Test Mail from Python Script"

    body = """Jay Ganesh,

This is a test email sent using Marvellous Python.

Regards,
Marvellous Infosystems
"""

    send_mail(sender_mail, app_password, reciever_email, subject, body)

print("Marvellous Mail Sent Successfully")

# ------------------------------------------------
# Program Entry Point
# ------------------------------------------------
if __name__ == "__main__":
    main()
