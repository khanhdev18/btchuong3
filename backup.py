import os
import schedule
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import shutil


load_dotenv()

EMAIL_SENDER ="leduykhanhhht@gmail.com"
EMAIL_PASSWORD = "aeyhozwlbxxmczaw"
EMAIL_RECEIVER = "lek96820@gmail.com"
BACKUP_DIR = os.getenv("BACKUP_DIR", "./backup")  

def backup_database():
    print("Starting database backup...")
    try:
      
        database_file = 'your_database.sqlite3' 
        backup_file = os.path.join(BACKUP_DIR, f"backup_{time.strftime('%Y%m%d_%H%M%S')}.sqlite3")
        
        
        if not os.path.exists(BACKUP_DIR):
            os.makedirs(BACKUP_DIR)

      
        shutil.copy(database_file, backup_file)
        send_email(True, backup_file)  
        print(f"Sao lưu thành công: {backup_file}")
    except Exception as e:
        send_email(False, str(e)) 
        print(f"Sao lưu thất bại: {e}")

def send_email(success, details):
    subject = "Database Backup Status"
    if success:
        body = f"Backup completed successfully.\nDetails:\n{details}"
    else:
        body = f"Backup failed.\nError:\n{details}"

    msg = MIMEMultipart()
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("Email đã được gửi thành công.")
    except Exception as e:
        print(f"Email không được gửi thất bại: {e}")


# Schedule backup at 00:00 (midnight) every day
schedule.every().day.at("00:00").do(backup_database)

print("Backup job scheduled. Running...")

# Run scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)
