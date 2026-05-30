import streamlit as st
import pandas as pd


def dashboard_page(cursor, conn):

    st.title("📊 College Dashboard")

    # ==========================
    # TOTAL STUDENTS
    # ==========================

    cursor.execute(
        "SELECT COUNT(*) FROM students"
    )

    total_students = cursor.fetchone()[0]

    # ==========================
    # TOTAL TEACHERS
    # ==========================

    cursor.execute(
        "SELECT COUNT(*) FROM teachers"
    )

    total_teachers = cursor.fetchone()[0]

    # ==========================
    # TOTAL FEES
    # ==========================

    cursor.execute(
        "SELECT SUM(paid_fee) FROM fees"
    )

    fee_result = cursor.fetchone()[0]

    total_fees = (
        fee_result
        if fee_result
        else 0
    )

    # ==========================
    # DASHBOARD CARDS
    # ==========================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Students",
            total_students
        )

    with col2:

        st.metric(
            "Teachers",
            total_teachers
        )

    with col3:

        st.metric(
            "Fees Collected",
            f"₹{total_fees}"
        )

    st.divider()

    st.subheader(
        "📋 Recent Students"
    )

    df = pd.read_sql_query(
        """
        SELECT *
        FROM students
        ORDER BY student_id DESC
        LIMIT 10
        """,
        conn
    )

    st.dataframe(
        df,
        use_container_width=True
    )