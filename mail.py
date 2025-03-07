
from email.message import EmailMessage
import ssl
import smtplib

def send_email(name, location, mail_receiver):

    mail_sender = ''
    mail_password = ''

    
    subject = 'Missing Person - Match Found'
    lat, long = location[0], location[1]
    body = f"There is a person who matches to the your missing report\nName: {name}\nLocation: {lat, long}"

    em = EmailMessage()
    em['From'] = mail_sender
    em['To'] = mail_receiver
    em['subject'] = subject

    em.set_content(body)
    with open('detected_image.jpg', 'rb') as f:
        img_data = f.read()
        em.add_attachment(img_data, maintype='image', subtype='jpg', filename='detected_image.jpg')

    # send the email using SMTP
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(mail_sender, mail_password)
        smtp.send_message(em)




