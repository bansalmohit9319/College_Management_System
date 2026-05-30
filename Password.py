import streamlit as st

from Security import (
    change_password
)


def change_password_page(
    cursor,
    conn
):

    st.header(
        "🔒 Change Password"
    )

    username = st.text_input(
        "Username"
    )

    new_password = st.text_input(
        "New Password",
        type="password"
    )

    if st.button(
        "Update Password"
    ):

        change_password(
            cursor,
            conn,
            username,
            new_password
        )

        st.success(
            "Password Updated"
        )