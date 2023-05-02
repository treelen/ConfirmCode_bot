
from dotenv import load_dotenv
import smtplib,os
from email.message import EmailMessage
load_dotenv('.env')

def send_mail(title:str , message:str,to_user:str ) -> str:
    sender  = os.environ.get('smtp_email')
    password = os.environ.get('smtp_password')
    
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    
    msg = EmailMessage()
    msg['Subject'] = title 
    msg['From'] = os.environ.get('SMTP_EMAIL')
    msg['To'] = to_user
    msg.set_content(message)
    try:
        server.login(sender,password)
        server.send_message(msg)
        return 'Send Mail to me '
    except Exception as error:
        return f'Error {error}'
    
# print(send_mail("hello","geeks 0",'marzybek117788@gmail.com'))

emails = ['marzybek117788@gmail.com','marzybek1177@gmail.com']
def sending_mail(email_list:list) -> str:
    for email in email_list:
        print(email)
        

sending_mail(emails)