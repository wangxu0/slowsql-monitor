# -*- coding: utf-8 -*-

import content_formatter
import ConfigParser
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


parser = ConfigParser.ConfigParser()
parser.read("../monitor.conf")
host = parser.get("config", "mail_host")
port = parser.get("config", "mail_port")
addr = parser.get("config", "mail_addr")
pswd = parser.get("config", "mail_pswd")


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr.encode('utf-8') if isinstance(addr, unicode) else addr))


def send_email(email_list, subject, content_list):
    msg = MIMEText(content_formatter.format_content(content_list), 'html', 'utf-8')
    msg['From'] = _format_addr(u'MySQL Slow SQL Monitor <%s>' % addr)
    msg['To'] = _format_addr(u'Administrator <%s>' % email_list[0])
    msg['Subject'] = Header(subject, 'utf-8').encode()

    server = smtplib.SMTP(host, port)
    server.set_debuglevel(1)
    server.login(addr, pswd)
    server.sendmail(addr, email_list, msg.as_string())
    server.quit()
