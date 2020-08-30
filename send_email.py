from credentials import email, password


import smtplib
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

server.login(email, password)
server.sendmail(email, email, "This is my test message")

server.quit()
print('email sent')