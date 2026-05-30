import streamlit as st
import pandas as pd
from datetime import date


def create_attendance_table(
    cursor,
    conn
):

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        attendance_date TEXT,
        status TEXT
    )
    """)

    conn.commit()


def attendance_page(
    cursor,
    conn
):

    st.header(
        "📅 Attendance Management"
    )

    option = st.selectbox(
        "Select Option",
        [
            "Mark Attendance",
            "View Attendance"
        ]
    )

    # =====================================
    # MARK ATTENDANCE
    # =====================================

    if option == "Mark Attendance":

        student_id = st.number_input(
            "Student ID",
            min_value=1
        )

        attendance_date = st.date_input(
            "Date",
            value=date.today()
        )

        status = st.selectbox(
            "Status",
            [
                "Present",
                "Absent"
            ]
        )

        if st.button(
            "Save Attendance"
        ):

            cursor.execute(
                """
                INSERT INTO attendance
                (
                    student_id,
                    attendance_date,
                    status
                )
                VALUES(?,?,?)
                """,
                (
                    student_id,
                    str(attendance_date),
                    status
                )
            )

            conn.commit()

            st.success(
                "Attendance Saved Successfully"
            )

    # =====================================
    # VIEW ATTENDANCE
    # =====================================

    elif option == "View Attendance":

        query = """
        SELECT * FROM attendance
        """

        df = pd.read_sql_query(
            query,
            conn
        )

        st.dataframe(
            df,
            use_container_width=True
        )