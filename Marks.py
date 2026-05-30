import streamlit as st
import pandas as pd


def create_marks_table(cursor, conn):

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS marks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        subject TEXT,
        marks INTEGER
    )
    """)

    conn.commit()


def marks_page(cursor, conn):

    st.header("📝 Marks Management")

    option = st.selectbox(
        "Select Option",
        [
            "Add Marks",
            "View Marks",
            "Delete Marks"
        ]
    )

    # =========================
    # ADD MARKS
    # =========================

    if option == "Add Marks":

        student_id = st.number_input(
            "Student ID",
            min_value=1
        )

        subject = st.text_input(
            "Subject"
        )

        marks = st.number_input(
            "Marks",
            min_value=0,
            max_value=100
        )

        if st.button("Save Marks"):

            cursor.execute(
                """
                INSERT INTO marks
                (
                    student_id,
                    subject,
                    marks
                )
                VALUES(?,?,?)
                """,
                (
                    student_id,
                    subject,
                    marks
                )
            )

            conn.commit()

            st.success(
                "Marks Saved Successfully"
            )

    # =========================
    # VIEW MARKS
    # =========================

    elif option == "View Marks":

        df = pd.read_sql_query(
            """
            SELECT * FROM marks
            """,
            conn
        )

        st.dataframe(
            df,
            use_container_width=True
        )

    # =========================
    # DELETE MARKS
    # =========================

    elif option == "Delete Marks":

        record_id = st.number_input(
            "Record ID",
            min_value=1
        )

        if st.button(
            "Delete Marks"
        ):

            cursor.execute(
                """
                DELETE FROM marks
                WHERE id=?
                """,
                (
                    record_id,
                )
            )

            conn.commit()

            st.success(
                "Marks Deleted"
            )