import cv2
from pyzbar.pyzbar import decode
import pandas as pd
import datetime
import smtplib
from email.mime.text import MIMEText

# Load student data
students_df = pd.read_csv("C:\\Users\\rpadm\\OneDrive\\Desktop\\Tushar\\students.csv")

# Track attendance
present_students = set()

print("📷 Starting Camera... Press ESC to stop")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    for code in decode(frame):
        reg_no = code.data.decode('utf-8')

        if reg_no not in present_students:
            present_students.add(reg_no)
            print(f"✅ Marked Present: {reg_no}")

    cv2.imshow("QR Attendance Scanner", frame)

    if cv2.waitKey(1) == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()

# Generate attendance report
students_df["Status"] = students_df["RegNo"].apply(
    lambda x: "Present" if x in present_students else "Absent"
)

# Save to Excel
date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_name = f"C:\\Users\\rpadm\\OneDrive\\Desktop\\Tushar\\attendance_{date}.xlsx"
students_df.to_excel(file_name, index=False)

print(f"\n📄 Attendance saved as {file_name}")

# ------------------ EMAIL PART ------------------

def send_email(file_name):
    sender_email = "tusharmanju17232@gmail.com"
    receiver_email = "tusharmanju1723@gmail.com"
    app_password = "tusharmanju@gmail.com"  # Use Gmail App Password

    # Create email
    msg = MIMEText(f"Attendance Report Attached: {file_name}")
    msg['Subject'] = "Smart Attendance Report"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(msg)
        server.quit()
        print("📧 Email Sent Successfully!")
    except Exception as e:
        print("❌ Email Failed:", e)

# Send email
send_email(file_name)