import streamlit as st
import sqlite3

from Student import create_student_table, student_page
from Teacher import create_teacher_table, teacher_page
from Attendance import create_attendance_table, attendance_page
from Marks import create_marks_table, marks_page
from Fees import create_fees_table, fees_page
from Dashboard import dashboard_page
from Report import reports_page
from Password import change_password_page
from Login import login_page

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="College Management System",
    layout="wide"
)

# ==========================
# DATABASE CONNECTION
# ==========================

conn = sqlite3.connect(
    "college.db",
    check_same_thread=False
)

cursor = conn.cursor()

# ==========================
# USERS TABLE
# ==========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

conn.commit()

# ==========================
# CREATE ALL TABLES
# ==========================

create_student_table(cursor, conn)
create_teacher_table(cursor, conn)
create_attendance_table(cursor, conn)
create_marks_table(cursor, conn)
create_fees_table(cursor, conn)

# ==========================
# TITLE
# ==========================

st.title("🎓 College Management System")

# ==========================
# MENU
# ==========================

menu = st.sidebar.selectbox(
    "Select Module",
    [
        "Dashboard",
        "Students",
        "Teachers",
        "Attendance",
        "Marks",
        "Fees",
        "Reports",
        "Change Password",
        "Login"
    ]
)

# ==========================
# ROUTING
# ==========================

if menu == "Dashboard":
    dashboard_page(cursor, conn)

elif menu == "Students":
    student_page(cursor, conn)

elif menu == "Teachers":
    teacher_page(cursor, conn)

elif menu == "Attendance":
    attendance_page(cursor, conn)

elif menu == "Marks":
    marks_page(cursor, conn)

elif menu == "Fees":
    fees_page(cursor, conn)

elif menu == "Reports":
    reports_page(conn)

elif menu == "Change Password":
    change_password_page(cursor, conn)

elif menu == "Login":
    login_page(cursor)