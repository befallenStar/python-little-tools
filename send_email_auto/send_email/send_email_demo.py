# -*- encoding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
import configparser
from send_email_auto.load_config.load import read_config


def load_default_config():
    default_config=r'C:\Users\ThinkPad\.sendEmail\config.ini'
    cf=configparser.ConfigParser()
    if not os.path.exists(default_config):
        with open(r'C:\Users\ThinkPad\.sendEmail\config.ini','w') as f:
            f.write('[config]\naddress=./config.ini')
        cf.write(f)
    cf.read(r'C:\Users\ThinkPad\.sendEmail\config.ini')
    config_address=cf.get('config','address')
    return config_address


def main():
    email_config=read_config(load_default_config())

    mail_host=email_config['smtp']
    mail_user=email_config['user']
    mail_pwd=email_config['pwd']

    # sender='sy5622_5@126.com'
    receivers=email_config['to']
    message=MIMEText('demo test','plain','utf-8')
    message['From']=mail_user
    message['To']=receivers
    message['Subject']=Header('demo test','utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host,25)
        smtpObj.login(mail_user,mail_pwd)
        smtpObj.sendmail(mail_user, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print(str(e))
        print("Error: 无法发送邮件")


if __name__ == '__main__':
    main()