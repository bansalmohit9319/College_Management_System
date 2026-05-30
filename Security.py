import hashlib


# ==========================
# HASH PASSWORD
# ==========================

def hash_password(password):

    return hashlib.sha256(
        password.encode()
    ).hexdigest()


# ==========================
# VERIFY PASSWORD
# ==========================

def verify_password(
    input_password,
    stored_password
):

    return (
        hash_password(
            input_password
        )
        ==
        stored_password
    )

def change_password(
    cursor,
    conn,
    username,
    new_password
):

    hashed_password = hash_password(
        new_password
    )

    cursor.execute(
        """
        UPDATE users
        SET password=?
        WHERE username=?
        """,
        (
            hashed_password,
            username
        )
    )

    conn.commit()