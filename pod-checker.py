import os
from kubernetes import client, config
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


config.load_kube_config()


v1 = client.CoreV1Api()


pending_pods = []
for pod in v1.list_pod_for_all_namespaces().items:
    if pod.status.phase == "Pending":
        pending_pods.append(pod.metadata.name)

# Send email if pending pods found
if pending_pods:
    from_address = "devops.savitha@gmail.com"
    to_address = "mk.savitha16@gmail.com"
    subject = "Pending Pods Alert"
    body = f"Pending pods found: {', '.join(pending_pods)}"

    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "devops.savitha@gmail.com"
    smtp_password = "Humber@123"

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(from_address, to_address, msg.as_string())
    server.quit()
