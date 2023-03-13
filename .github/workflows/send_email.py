import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email_user = os.environ.get('EMAIL_USER')
email_pass = os.environ.get('EMAIL_PASS')

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = 'abdhulhakkim786@gmail.com'
msg['Subject'] = 'GitHub push notification'

body = 'A push event has occurred in the main branch!'
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_user, email_pass)
text = msg.as_string()
server.sendmail(email_user, 'abdhulhakkim786@gmail.com', text)
server.quit()
