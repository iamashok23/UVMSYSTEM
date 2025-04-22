# 🎓 College Management System - Python Console Project

This is a **Python-based console application** that simulates a basic **College Management System**. The project features a secure **OTP-based login system** and provides different modules for managing students, faculty, and courses in a university environment.

## 🔐 Features

- **Secure Login** using OTP sent via Email
- **Student Management** (Add, View, Update, Delete)
- **Faculty Management** (Add, View, Update, Delete)
- **Course Management**
- Modular structure for better code readability
- Console-based UI for user interaction

## 🛠 Technologies Used

- **Python** (core language)
- **smtplib** and **email** modules for OTP delivery
- **Random** for OTP generation
- **Datetime**, **OS**, etc., for utility functions

## 📁 Project Structure

```
college_management_system/
│
├── main.py                  # Entry point with menu-driven logic
├── otp_verification.py      # Handles OTP generation and email sending
├── student_module.py        # Functions to manage student data
├── faculty_module.py        # Functions to manage faculty data
├── course_module.py         # Course-related operations
└── utils.py                 # Helper functions
```

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/college-management-system.git
   cd college-management-system
   ```

2. Make sure to update the email credentials in `otp_verification.py` for OTP delivery.

3. Run the main script:
   ```bash
   python main.py
   ```

## 📌 Note

- Use a secure app password for Gmail to avoid authentication issues.
- This is a **console-based project** suitable for learning purposes and beginner-level practice.

## 📷 Demo

*(You can add screenshots or a short demo GIF here)*

## 🙌 Contributions

Contributions are welcome! Feel free to fork the repo and submit a pull request.

## 📧 Contact

Created by **Ashok** — [LinkedIn](https://www.linkedin.com/in/your-profile)  
For any inquiries or feedback, feel free to connect!
