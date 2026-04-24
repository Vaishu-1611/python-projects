import pandas as pd
from datetime import datetime

FILE_NAME = "attendance.csv"


def mark_attendance():
    name = input("Enter student name: ")
    status = input("Enter status (P/A): ")

    time_now = datetime.now()
    date = time_now.strftime('%Y-%m-%d')
    time = time_now.strftime('%H:%M:%S')

    new_data = pd.DataFrame({
        "Name": [name],
        "Status": [status],
        "Date": [date],
        "Time": [time]
    })

    try:
        old_data = pd.read_csv(FILE_NAME)
        updated_data = pd.concat([old_data, new_data], ignore_index=True)
    except FileNotFoundError:
        updated_data = new_data

    updated_data.to_csv(FILE_NAME, index=False)

    print("Attendance marked successfully!")


def show_summary():
    try:
        df = pd.read_csv(FILE_NAME)

        print("\n Attendance Summary:")
        print(df["Status"].value_counts())

    except:
        print("No data found!")


def show_leaderboard():
    try:
        df = pd.read_csv(FILE_NAME)

        present_count = df[df["Status"] == "P"]["Name"].value_counts()

        print("\n Top Attendance:")
        print(present_count.head())

    except:
        print("No data found!")


def low_attendance_warning():
    try:
        df = pd.read_csv(FILE_NAME)

        total = df["Name"].value_counts()
        present = df[df["Status"] == "P"]["Name"].value_counts()

        percentage = (present / total) * 100

        print("\n Low Attendance (<75%):")
        print(percentage[percentage < 75])

    except:
        print("No data found!")


def view_all():
    try:
        df = pd.read_csv(FILE_NAME)
        print("\n Full Attendance Record:")
        print(df)
    except:
        print("No data found!")


# Main Menu
while True:
    print("\n===== Attendance Tracker =====")
    print("1. Mark Attendance")
    print("2. View Summary")
    print("3. Leaderboard")
    print("4. Low Attendance Warning")
    print("5. View All Records")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        mark_attendance()
    elif choice == "2":
        show_summary()
    elif choice == "3":
        show_leaderboard()
    elif choice == "4":
        low_attendance_warning()
    elif choice == "5":
        view_all()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")