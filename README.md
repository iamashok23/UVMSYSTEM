# 🎓 College Management System (Console-Based) with OTP Login

Welcome to my **College Management System**, a console-based Python project that simulates a mini university administration environment with secure access via **OTP-based login**.

## 🔐 Features

- **OTP-Based Login System** for secure access (via email)
- **Student Management**  
  - Add new students  
  - View student details  
  - Search and update student information  
- **Faculty Management**  
  - Add faculty members  
  - View faculty details  
  - Search and update faculty records  
- **Course Management**  
  - Add and manage courses  
  - Assign courses to students and faculty  
- **Attendance Management**  
  - Record and view attendance  
- **Marks Entry & Report**  
  - Add and update marks  
  - Generate reports  
- **Modular Codebase** for better readability and maintenance

## 🛠 Technologies Used

- **Python** (Core logic)
- **SMTP (smtplib)** for OTP email delivery
- **Random** for OTP generation
- **Datetime** for timestamps
- **File handling / Dictionaries** for data management

## 📁 Project Structure

```
CollegeManagementSystem/
|
├── main.py                  # Entry point of the system
├── otp_login.py            # OTP-based login logic
├── student.py              # Student-related functions
├── faculty.py              # Faculty-related functions
├── course.py               # Course and subject management
├── attendance.py           # Attendance tracking
├── marks.py                # Marks and report generation
├── utils.py                # Helper functions and validations
└── README.md               # Project documentation
```

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/CollegeManagementSystem.git
   cd CollegeManagementSystem
   ```

2. Make sure you have Python 3 installed.

3. Run the project:
   ```bash
   python main.py
   ```

> **Note**: To send OTP via email, make sure to enable "Less secure app access" or use an **App Password** for Gmail SMTP access.

## 📬 Feedback

Have suggestions or want to collaborate? Feel free to reach out or open an issue!

---

✅ *This project is a part of my learning journey as a Python developer. More features and improvements are on the way!*

