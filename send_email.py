import smtplib
import sys
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

try:
  #email_user = os.environ.get('EMAIL_USER')
  #email_pass = os.environ.get('EMAIL_PASS')
  email_user = 'abdhulhakkim0@gmail.com'
  email_pass = 'scydcayxqieyufzj'
  
  print("hai ji")
  print(email_user, flush=True)

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
  
except Exception as e:
  print(f"Error: {e}", file=sys.stderr)
  print(email_user)
  sys.exit(1)
