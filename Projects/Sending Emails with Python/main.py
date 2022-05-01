import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Rajesh Arya'
email['to'] = 'rajesh_creator@live.com'
email['subject'] = ' This is a test email'

email.set_content('This is my first email using python !!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('rajeshkumara6@gmail.com', 'Imra@111')
    smtp.send_message(email)
    print('Email has been sent)')