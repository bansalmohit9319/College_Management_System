import streamlit as st

from Security import (
    verify_password
)


def login_page(
    cursor
):

    st.title(
        "🎓 College Management System"
    )

    st.subheader(
        "Secure Login"
    )

    username = st.text_input(
        "Username"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        cursor.execute(
            """
            SELECT password
            FROM users
            WHERE username=?
            """,
            (
                username,
            )
        )

        result = cursor.fetchone()

        if result:

            stored_password = result[0]

            if verify_password(
                password,
                stored_password
            ):

                st.session_state.logged_in = True

                st.success(
                    "Login Successful"
                )

                st.rerun()

            else:

                st.error(
                    "Wrong Password"
                )

        else:

            st.error(
                "User Not Found"
            )