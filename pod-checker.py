from kubernetes import client, config
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time


def get_pending():
   config.load_incluster_config()
   v1 = client.CoreV1Api()
   results = []

   pending_pods = v1.list_pod_for_all_namespaces(field_selector="status.phase=Pending").items

   for pod in pending_pods:
      pod_detail = {
         "Name": pod.metadata.name,
         "Pending Since": pod.metadata.creation_timestamp.strftime('%Y-%m-%d %H:%M:%S %Z')
      }
      results.append(pod_detail)

   return results


def write_to_file():
   file_path = "/data/pending-pods.log"
   message = ""

   for pod in get_pending():
      message += f"Pod Name: {pod['Name']}\n"
      message += f"Pending Since: {pod['Pending Since']}\n"

   with open(file_path, "a+") as file:
      file.write(message + "\n")

def send_email():
   smtp_server = "smtp.gmail.com"
   smtp_port = 587
   smtp_username = "devops.savitha@gmail.com"
   smtp_password = "mngylfjjimfdoqag"

   sender_email = "devops.savitha@gmail.com"
   receiver_email = "mk.savitha16@gmail.com"
   subject = "Pending Pods Alert"
   message = ""

   for pod in get_pending():
      message += f"Pod Name: {pod['Name']}\n"
      message += f"Pending Since: {pod['Pending Since']}\n"
      message += "---\n"

   msg = MIMEMultipart()
   msg['From'] = sender_email
   msg['To'] = receiver_email
   msg['Subject'] = subject
   msg.attach(MIMEText(message, 'plain'))

   try:
      server = smtplib.SMTP(smtp_server, smtp_port)
      server.starttls()
      server.login(smtp_username, smtp_password)
      server.sendmail(sender_email, receiver_email, msg.as_string())
      print("Email sent successfully!")
   except Exception as e:
      print(f"Error sending email: {e}")
   finally:
      server.quit()

send_email()
write_to_file()

time.sleep(10)

send_email()
write_to_file()

time.sleep(10)

send_email()
write_to_file()

time.sleep(10)

send_email()
write_to_file()

time.sleep(10)

send_email()
write_to_file()

time.sleep(10)

send_email()
write_to_file()

