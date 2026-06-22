import qrcode
import csv
import os


students = [
    ("251127CSR092", "Tushar"),
    ("251127CSR098", "Yogesh"),
    ("251127CSR089", "Suresh"),
    ("251127CSR060", "Pritish"),
    ("251127CSR057", "Prakash")
    
]

# Create folder
if not os.path.exists("C:\\Users\\rpadm\\OneDrive\\Desktop\\Tushar\\qrcode"):
    os.makedirs("C:\\Users\\rpadm\\OneDrive\\Desktop\\Tushar\\qrcode")

# Generate QR codes
for reg_no, name in students:
    data = f"{reg_no}"
    img = qrcode.make(data)
    img.save(f"C:\\Users\\rpadm\\OneDrive\\Desktop\\Tushar\\qrcode\\{reg_no}.png")

# Save student list
with open("C:\\Users\\rpadm\\OneDrive\\Desktop\\Tushar\\students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["RegNo", "Name"])
    writer.writerows(students)

print("QR Codes Generated Successfully!")