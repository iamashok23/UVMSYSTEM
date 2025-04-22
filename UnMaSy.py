import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

def otp(to_email):
    otp = random.randint(1111,9999)

    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    username = "ashokmangali631@gmail.com"
    password = "injq lofl pivt cddh"

    from_email = "ashokmangali631@gmail.com"
    subject = "OTP for verification"
    body = f"The OTP for Verification is {otp}"

    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body,"plain"))

    server = smtplib.SMTP(smtp_server,smtp_port)
    server.starttls()
    server.login(username,password)
    server.send_message(msg)
    server.quit()
    print("Email sent !")

    votp = int(input("Enter Otp: "))
    if votp == otp:
        print("Verification Success")
        return True
    else:
        print("Verification Failed")
        return False
        
    
    

colleges = []

class person:
    def __init__(self, rollno, name, email):
        self.rollno = rollno
        self.name = name
        self.email = email

class student(person):
    def __init__(self, rollno, name, branch, email):
        super().__init__(rollno, name, email)
        self.branch = branch

class teacher(person):
    def __init__(self, rollno, name, subject, email):
        super().__init__(rollno, name, email)
        self.subject = subject

class college:
    def __init__(self, clg_id, clg_name):
        self.clg_id = clg_id
        self.clg_name = clg_name
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

print("Welcome to College Management System!\n")

while True:
    print("1. Add College")
    print("2. Add Student")
    print("3. Add Teacher")
    print("4. Login as Student")
    print("5. Login as Teacher")
    print("6. Exit")

    x = int(input("Enter Your Choice: "))

    if x == 1:
        clg_id = int(input("Enter College Id: "))
        if not any(c.clg_id == clg_id for c in colleges):
            clg_name = input("Enter College Name: ")
            colleges.append(college(clg_id, clg_name))
            print("College Added Successfully!\n")
        else:
            print("College Already Exists!\n")

    elif x == 2:
        clg_id = int(input("Enter College Id: "))
        college_obj = next((c for c in colleges if c.clg_id == clg_id), None)
        if college_obj:
            roll = int(input("Enter Student Roll No: "))
            name = input("Enter Student Name: ")
            branch = input("Enter Branch: ")
            email = input("Enter Email: ")
            s = student(roll, name, branch, email)
            college_obj.add_student(s)
            print("Student Added Successfully!\n")
        else:
            print("College Not Found!\n")

    elif x == 3:
        clg_id = int(input("Enter College Id: "))
        college_obj = next((c for c in colleges if c.clg_id == clg_id), None)
        if college_obj:
            roll = int(input("Enter Teacher Roll No: "))
            name = input("Enter Teacher Name: ")
            subject = input("Enter Subject: ")
            email = input("Enter Email: ")
            t = teacher(roll, name, subject, email)
            college_obj.add_teacher(t)
            print("Teacher Added Successfully!\n")
        else:
            print("College Not Found!\n") 

    elif x == 4:
        email = input("Enter Student Email: ")
        if otp(email):
            print("Login Successful!\n")
            
        else:
            print("Login Failed!\n")
            

    elif x == 5:
        email = input("Enter Teacher Email: ")
        if otp(email):
            print("Login Successful!\n")
            
        else:
            print("Login Failed!\n")
            

    elif x == 6:
        print("\nThank you, Visit Again!")
        
        break

    else:
        print("Invalid Choice!\n")
