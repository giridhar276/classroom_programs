 
import smtplib
from email.mime.text import MIMEText


# provide your SMTP ip address

s = smtplib.SMTP("172.30.42.127", 25)
#s.login("user","password")      # if SMTP is password protected

try:
 
    m = "This is a message from the last session"
    s.sendmail("giridhar276@gmail.com", "giridhar276@gmail.com", m)
 
    print("Finished sending message")
except Exception as e:
    print("Unable to send message: ", e)

s.quit()
