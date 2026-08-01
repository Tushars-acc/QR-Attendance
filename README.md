
# Smart QR Attendance System

A Python-based attendance management system that uses QR codes and a webcam to automatically record student attendance.

The system scans student QR codes, identifies students using their registration numbers, generates an attendance report in Excel format, and can email the report automatically.

## Features

- Generate unique QR codes for students
- Store student information in CSV format
- Scan QR codes using a webcam
- Automatically mark students as Present
- Identify students using their registration number
- Mark unscanned students as Absent
- Generate timestamped Excel attendance reports
- Automatically email attendance reports
- Prevent duplicate attendance entries during a session

## How It Works

```text
Student QR Code
       ↓
Webcam Scanner
       ↓
QR Code Detection
       ↓
Registration Number
       ↓
Student Database (CSV)
       ↓
Attendance Processing
       ↓
Excel Attendance Report
       ↓
Email Report
````

## Tech Stack

* Python
* OpenCV
* PyZbar
* Pandas
* QRCode
* CSV
* SMTP
* Excel / XLSX

## Project Structure

```text
smart-qr-attendance/
│
├── attendance.py
├── students.csv
├── qrcode/
│   ├── 251127CSR092.png
│   ├── 251127CSR098.png
│   └── ...
│
├── .gitignore
└── README.md
```

## Requirements

Python 3.9+ is recommended.

Install the required packages:

```bash
pip install opencv-python pyzbar pandas qrcode openpyxl
```

Depending on your operating system, PyZbar may also require the ZBar library.

## Student Data

The system uses a CSV file containing student registration numbers and names.

Example:

```csv
RegNo,Name
251127CSR092,Tushar
251127CSR098,Yogesh
251127CSR089,Suresh
251127CSR060,Pritish
251127CSR057,Prakash
```

## Usage

### 1. Configure the Student Data

Add students to the student list:

```python
students = [
    ("251127CSR092", "Tushar"),
    ("251127CSR098", "Yogesh"),
    ("251127CSR089", "Suresh"),
]
```

### 2. Generate QR Codes

The system generates a unique QR code for each student's registration number.

Each QR code contains the student's unique registration number.

### 3. Start the Attendance Scanner

Run:

```bash
python attendance.py
```

The webcam will open and begin scanning QR codes.

When a QR code is detected, the system records the student's registration number:

```text
✅ Marked Present: 251127CSR092
```

The student is added to the attendance list.

Press **ESC** to stop scanning.

### 4. Attendance Report

After scanning is complete, the system compares the scanned registration numbers against the student database.

Students are automatically assigned one of two statuses:

* `Present` — QR code was scanned
* `Absent` — QR code was not scanned

An Excel report is then generated with a timestamp.

Example:

```text
attendance_2026-08-01_14-30-22.xlsx
```

## Email Reports

The system can automatically send the generated attendance report through Gmail SMTP.

For security, email credentials should **never be stored directly in the source code**.

Use environment variables instead:

```python
import os

sender_email = os.getenv("SENDER_EMAIL")
receiver_email = os.getenv("RECEIVER_EMAIL")
app_password = os.getenv("EMAIL_APP_PASSWORD")
```

Create a `.env` file locally:

```text
SENDER_EMAIL=your-email@gmail.com
RECEIVER_EMAIL=recipient@gmail.com
EMAIL_APP_PASSWORD=your-app-password
```

Never commit the `.env` file to GitHub.

## Security

This project handles student information and email credentials.

Before publishing the project:

* Never commit Gmail passwords or app passwords
* Never commit private student data
* Never commit generated attendance reports
* Never commit personal Windows file paths
* Use environment variables for credentials
* Add sensitive files to `.gitignore`

Example `.gitignore`:

```gitignore
.env
*.xlsx
__pycache__/
*.pyc
.vscode/
.idea/
```

## Limitations

The current version is designed as a simple local attendance system.

Current limitations include:

* Requires a webcam
* Requires QR codes to be generated beforehand
* Uses a local CSV file as the student database
* Attendance reports are stored locally
* Email configuration requires Gmail SMTP setup
* No graphical dashboard or web interface
* No authentication system
* No cloud database

## Future Improvements

Possible improvements include:

* Web-based attendance dashboard
* MySQL/PostgreSQL database
* Student login system
* Teacher/admin authentication
* Attendance history and analytics
* Monthly attendance reports
* Automatic email scheduling
* Export to CSV/PDF
* Mobile QR scanning
* Cloud deployment
* Better error handling and logging
* Attendance analytics and visualization

## Learning Outcomes

This project provided hands-on experience with:

* Computer vision using OpenCV
* QR code detection and generation
* CSV data processing
* Pandas data manipulation
* Excel report generation
* Webcam-based real-time processing
* SMTP email automation
* Python file handling
* Basic automation workflows

## Author

**Tushar S**

Computer Science Engineering Student

GitHub: @Tushars-acc


