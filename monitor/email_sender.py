import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr.encode('utf-8') if isinstance(addr, unicode) else addr))


def send_email(emails, subject, content):
    from_addr = "mysqlslowsql@126.com"
    password = "123456"
    msg = MIMEText(content, 'html', 'utf-8')
    msg['From'] = _format_addr(u'MySQL Slow SQL Monitor <%s>' % from_addr)
    msg['To'] = _format_addr(u'管理员 <%s>' % emails[0])
    msg['Subject'] = Header(subject, 'utf-8').encode()

    server = smtplib.SMTP("126", 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, emails, msg.as_string())
    server.quit()
