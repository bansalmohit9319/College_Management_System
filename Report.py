import streamlit as st
import pandas as pd


def reports_page(conn):

    st.header(
        "📄 Reports Export"
    )

    report_type = st.selectbox(
        "Select Report",
        [
            "Students",
            "Teachers",
            "Attendance",
            "Marks",
            "Fees"
        ]
    )

    # ==========================
    # STUDENTS REPORT
    # ==========================

    if report_type == "Students":

        df = pd.read_sql_query(
            "SELECT * FROM students",
            conn
        )

    # ==========================
    # TEACHERS REPORT
    # ==========================

    elif report_type == "Teachers":

        df = pd.read_sql_query(
            "SELECT * FROM teachers",
            conn
        )

    # ==========================
    # ATTENDANCE REPORT
    # ==========================

    elif report_type == "Attendance":

        df = pd.read_sql_query(
            "SELECT * FROM attendance",
            conn
        )

    # ==========================
    # MARKS REPORT
    # ==========================

    elif report_type == "Marks":

        df = pd.read_sql_query(
            "SELECT * FROM marks",
            conn
        )

    # ==========================
    # FEES REPORT
    # ==========================

    elif report_type == "Fees":

        df = pd.read_sql_query(
            "SELECT * FROM fees",
            conn
        )

    st.dataframe(
        df,
        use_container_width=True
    )

    csv = df.to_csv(
        index=False
    ).encode(
        "utf-8"
    )

    st.download_button(
        label="⬇ Download CSV",
        data=csv,
        file_name=f"{report_type}.csv",
        mime="text/csv"
    )