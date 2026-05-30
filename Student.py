import streamlit as st
import pandas as pd


def create_student_table(cursor, conn):

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        student_id INTEGER PRIMARY KEY,
        name TEXT,
        course TEXT,
        email TEXT,
        phone TEXT,
        semester INTEGER
    )
    """)

    conn.commit()


def student_page(cursor, conn):

    st.header("🎓 Student Management")

    option = st.selectbox(
        "Select Option",
        [
            "Add Student",
            "View Students",
            "Delete Student"
        ]
    )

    # ADD STUDENT
    if option == "Add Student":

        sid = st.number_input(
            "Student ID",
            min_value=1
        )

        name = st.text_input(
            "Student Name"
        )

        course = st.text_input(
            "Course"
        )

        email = st.text_input(
            "Email"
        )

        phone = st.text_input(
            "Phone"
        )

        semester = st.number_input(
            "Semester",
            min_value=1,
            max_value=8
        )

        if st.button("Save Student"):

            try:

                cursor.execute(
                    """
                    INSERT INTO students
                    VALUES(?,?,?,?,?,?)
                    """,
                    (
                        sid,
                        name,
                        course,
                        email,
                        phone,
                        semester
                    )
                )

                conn.commit()

                st.success(
                    "Student Added Successfully"
                )

            except:

                st.error(
                    "Student ID Already Exists"
                )

    # VIEW STUDENTS
    elif option == "View Students":

        df = pd.read_sql_query(
            """
            SELECT * FROM students
            """,
            conn
        )

        st.dataframe(
            df,
            use_container_width=True
        )

    # DELETE STUDENT
    elif option == "Delete Student":

        sid = st.number_input(
            "Student ID",
            min_value=1,
            key="delete_student"
        )

        if st.button(
            "Delete Student"
        ):

            cursor.execute(
                """
                DELETE FROM students
                WHERE student_id=?
                """,
                (
                    sid,
                )
            )

            conn.commit()

            st.success(
                "Student Deleted Successfully"
            )