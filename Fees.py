import streamlit as st
import pandas as pd


def create_fees_table(cursor, conn):

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS fees(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        total_fee INTEGER,
        paid_fee INTEGER
    )
    """)

    conn.commit()


def fees_page(cursor, conn):

    st.header("💰 Fees Management")

    option = st.selectbox(
        "Select Option",
        [
            "Add Fee Record",
            "View Fees"
        ]
    )

    # =========================
    # ADD FEES
    # =========================

    if option == "Add Fee Record":

        student_id = st.number_input(
            "Student ID",
            min_value=1
        )

        total_fee = st.number_input(
            "Total Fee",
            min_value=0
        )

        paid_fee = st.number_input(
            "Paid Fee",
            min_value=0
        )

        if st.button(
            "Save Fee Record"
        ):

            cursor.execute(
                """
                INSERT INTO fees
                (
                    student_id,
                    total_fee,
                    paid_fee
                )
                VALUES(?,?,?)
                """,
                (
                    student_id,
                    total_fee,
                    paid_fee
                )
            )

            conn.commit()

            st.success(
                "Fee Record Saved"
            )

    # =========================
    # VIEW FEES
    # =========================

    elif option == "View Fees":

        query = """
        SELECT *,
        (total_fee-paid_fee)
        AS pending_fee
        FROM fees
        """

        df = pd.read_sql_query(
            query,
            conn
        )

        st.dataframe(
            df,
            use_container_width=True
        )