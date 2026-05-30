import streamlit as st
import pandas as pd


def create_teacher_table(cursor, conn):

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS teachers(
        teacher_id INTEGER PRIMARY KEY,
        name TEXT,
        department TEXT,
        email TEXT,
        phone TEXT
    )
    """)

    conn.commit()


def teacher_page(cursor, conn):

    st.header("👨‍🏫 Teacher Management")

    option = st.selectbox(
        "Select Option",
        [
            "Add Teacher",
            "View Teachers",
            "Delete Teacher"
        ]
    )

    # =====================================
    # ADD TEACHER
    # =====================================

    if option == "Add Teacher":

        teacher_id = st.number_input(
            "Teacher ID",
            min_value=1
        )

        name = st.text_input(
            "Teacher Name"
        )

        department = st.text_input(
            "Department"
        )

        email = st.text_input(
            "Email"
        )

        phone = st.text_input(
            "Phone"
        )

        if st.button("Add Teacher"):

            try:

                cursor.execute(
                    """
                    INSERT INTO teachers
                    VALUES(?,?,?,?,?)
                    """,
                    (
                        teacher_id,
                        name,
                        department,
                        email,
                        phone
                    )
                )

                conn.commit()

                st.success(
                    "Teacher Added Successfully"
                )

            except:

                st.error(
                    "Teacher ID Already Exists"
                )

    # =====================================
    # VIEW TEACHERS
    # =====================================

    elif option == "View Teachers":

        query = """
        SELECT * FROM teachers
        """

        df = pd.read_sql_query(
            query,
            conn
        )

        st.dataframe(
            df,
            use_container_width=True
        )

    # =====================================
    # DELETE TEACHER
    # =====================================

    elif option == "Delete Teacher":

        teacher_id = st.number_input(
            "Teacher ID",
            min_value=1,
            key="delete_teacher"
        )

        if st.button(
            "Delete Teacher"
        ):

            cursor.execute(
                """
                DELETE FROM teachers
                WHERE teacher_id=?
                """,
                (
                    teacher_id,
                )
            )

            conn.commit()

            st.success(
                "Teacher Deleted Successfully"
            )