import db
import sqlite3


def test_create_admininfo_table():
    connection = sqlite3.connect(":memory:")

    db.create_admininfo_table(connection)

    connection.execute(
        "INSERT INTO AdminInfo(email, password) values ('abc@example.com', '123456')"
    )
    connection.execute(
        "INSERT INTO AdminInfo(email, password) values ('edf@example.com', 'password')"
    )

    cursor = connection.execute("SELECT * FROM AdminInfo")
    result = cursor.fetchall()
    assert len(result) == 2
    assert result[0] == (1, "abc@example.com", "123456")
    assert result[1] == (2, "edf@example.com", "password")

    connection.close()
