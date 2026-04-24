py -m pip install openpyxl
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Load Excel
book = openpyxl.load_workbook(r'D:\attendance.xlsx')
sheet = book['Sheet1']
r = sheet.max_row

staff_mails = ['erakshaya485@gmail.com', 'yyyyyyyy@gmail.com']

subjects = {
    1: ("CI", 3),
    2: ("Python", 4),
    3: ("DM", 5)
}


def savefile():
    book.save(r'D:\attendance.xlsx')
    print("Saved!")


def mailstu(li, msg):
    from_id = 'your_email@gmail.com'
    pwd = 'your_app_password'

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(from_id, pwd)

    for to_id in li:
        message = MIMEMultipart()
        message['Subject'] = 'Attendance Report'
        message.attach(MIMEText(msg, 'plain'))

        s.sendmail(from_id, to_id, message.as_string())

    s.quit()
    print("Mail sent to students")


def mailstaff(mail_id, msg):
    from_id = 'your_email@gmail.com'
    pwd = 'your_app_password'

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(from_id, pwd)

    message = MIMEMultipart()
    message['Subject'] = 'Lack of Attendance Report'
    message.attach(MIMEText(msg, 'plain'))

    s.sendmail(from_id, mail_id, message.as_string())
    s.quit()

    print("Mail sent to staff")


def check(no_of_days, row_num, subject_name, subject_code):

    students_warn = []
    students_fail = []
    roll_list = ""

    for i in range(len(row_num)):

        roll = sheet.cell(row=row_num[i], column=1).value
        email = sheet.cell(row=row_num[i], column=2).value
        days = no_of_days[i]

        if days == 2:
            students_warn.append(email)

        elif days > 2:
            students_fail.append(email)
            roll_list += str(roll) + " "

    if students_warn:
        mailstu(students_warn,
                f"Warning! Only 1 leave left in {subject_name}")

    if students_fail:
        msg1 = f"You have low attendance in {subject_name}"
        msg2 = f"Students with low attendance: {roll_list}"

        mailstu(students_fail, msg1)
        mailstaff(staff_mails[subject_code - 1], msg2)


while True:

    print("1-->CI\n2-->Python\n3-->DM")
    y = int(input("Enter subject: "))

    subject_name, col = subjects[y]

    n = int(input("No. of absentees: "))

    x = list(map(int, input("Roll nos: ").split()))

    row_num = []
    no_of_days = []

    for student in x:
        for i in range(2, r + 1):

            if sheet.cell(row=i, column=1).value == student:

                m = sheet.cell(row=i, column=col).value
                m = m + 1
                sheet.cell(row=i, column=col).value = m

                row_num.append(i)
                no_of_days.append(m)

                break

    savefile()

    check(no_of_days, row_num, subject_name, y)

    resp = int(input("Another subject? 1-->yes 0-->no: "))
    if resp == 0:
        break