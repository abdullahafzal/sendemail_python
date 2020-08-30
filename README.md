# sendemail_python

## What is SMTP Gmail?
Google's Gmail SMTP server is a free SMTP service which anyone who has a Gmail account can use to send emails. You can use it with personal emails, or even with your website if you are sending emails for things such as contact forms, newsletter blasts, or notifications.

## How to make a connection?
Start an SMTP connection that is secured from the beginning using SMTP_SSL().

## How to login?
server.login(email, password)

## How to send an email?
After you initiated a secure SMTP connection using either of the above methods, you can send your email using

server.sendmail(From_email, To_email, "This is the email message")
