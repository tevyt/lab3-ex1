import smtplib

fromaddr = 'travisinfo3180@gmail.com'
toaddr = 'travissmith94@hotmail.com'
fromname = 'Travis Smith'
toname = 'David Bain'
subject = 'test'
msg = 'test'
message = """From: {} <{}>
To: {} <{}>
Subject: {}

{}

"""

messagetosend = message.format(
        fromname,
        fromaddr,
        toname,
        toaddr,
        subject,
        msg)

username = 'travisinfo3180@gmail.com'
password = 'INFO3180'

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr , toaddr , messagetosend)
server.quit()
