##-----------------------------------------------------------------

##Real Python examples

##To check Using SMTP_SSL()

'''
import smtplib,ssl

smtp_server='smtp.gmail.com'
port=465

sender='--Enter your email address--'
password=input('Enter your password and press enter : ')

context=ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
    server.login(sender,password)
    ##print('It is working properly ')
'''

## To check Using TLS() connection
'''
import smtplib,ssl

smtp_server='smtp.gmail.com'
port=587

sender='--Enter your email address--'
password=input('Enter your password and press enter : ')

context=ssl.create_default_context()

with smtplib.SMTP(smtp_server,port) as server:
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender,password)
    print('It is working properly ')
'''
##-----------------------------------------------------------------

##Send you plain text mails
##1.Using SSL

'''
import smtplib,ssl

smtp_server='smtp.gmail.com'
port=465

sender='--Enter sender's email address--'
reciever='--Enter reciever's email address--'
password=input('Enter your password and press enter : ')

message="""\
From:{}
To:{}
Subject:Hi There! This message is sent from Python!
""".format(sender,reciever)


context=ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
    server.login(sender,password)
    server.sendmail(sender,reciever,message)

'''
##Using TLS
'''
import smtplib,ssl

smtp_server='smtp.gmail.com'
reciever='--Enter reciever's email address--'
port=587

sender='--Enter sender's email address--'
reciever='--Enter reciever's email address--'
password=input('Enter your password and press enter : ')

message="""\
From:{}
To:{}
Subject:Hi There! This message is sent from Python!
""".format(sender,reciever)

context=ssl.create_default_context()

with smtplib.SMTP(smtp_server,port) as server:
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender,password)
    server.sendmail(sender,reciever,message)
'''
##-----------------------------------------------------------------

## Including HTML content
'''
import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server='smtp.gmail.com'
port=465

sender=''--Enter sender's email address--'
reciever='--Enter reciever's email address--'
password=input('Enter your password and press enter : ')

message=MIMEMultipart()
message['Subject']='Email Automation'
message['From']=sender
message['To']=reciever

text="""\
Hi,
How are you? Hope everything is good!!"""

html="""\
<html><body>
<p>Hi, <br> How are you? Hope everything is good!!</p>
</body></html>
"""

part1=MIMEText(text,'plain')
part2=MIMEText(html,'html')
message.attach(part1)
message.attach(part2)

context=ssl.create_default_context()
msg=message.as_string()

with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
    server.login(sender,password)
    server.sendmail(sender,reciever,msg)
'''

##-----------------------------------------------------------------

##Adding attachments using email package

'''
import email,smtplib,ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_server='smtp.gmail.com'
port=465

subject='Email Automation using Python'
body='This is an email with attachment sent from python'
sender=''--Enter sender's email address--'
reciever='--Enter reciever's email address--'
password=input('Enter your password and press enter : ')

message=MIMEMultipart()
message['Subject']=subject
message['From']=sender
message['To']=reciever
message['Bcc']=reciever

message.attach(MIMEText(body,'plain'))

filename='Resume.docx'##Add Resume.docx file in your project

with open(filename,'rb') as f:
    part=MIMEBase('application','octet-stream')
    part.set_payload(f.read())

encoders.encode_base64(part)

part.add_header(
    'Content-Disposition',
     f"attachment; filename= {filename}",)

message.attach(part)

context=ssl.create_default_context()
msg=message.as_string()

with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
    server.login(sender,password)
    server.sendmail(sender,reciever,msg)
'''

##------------------------------------------------------------

##To send mail to multiple users using excel file
'''
import pandas as pd
import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server='smtp.gmail.com'
port=587

sender='--Enter sender's email address--'
password=input('Enter your password and press enter : ')

message=MIMEMultipart()
message['Subject']='Sending mails from excel sheet'
message['From']=sender

text="""\
Hi,
How are you? Hope everything is good!! This mail is sent to the users read from excel sheet"""

message.attach(MIMEText(text,'plain'))
body=message.as_string()

e=pd.read_excel('email.xlsx')
emails=e['Emails'].values

context=ssl.create_default_context()

server=smtplib.SMTP(smtp_server,port)
server.ehlo()
server.starttls(context=context)
server.ehlo()
server.login(sender,password)
for email in emails:
    server.sendmail(sender,email,body)
server.quit()
'''
##------------------------------------------------------

##To send mail to multiple users using csv file

'''
import csv

with open("contacts_file.csv") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for name, email, grade in reader:
        print(f"Sending email to {name}")
        # Send email here
'''





















