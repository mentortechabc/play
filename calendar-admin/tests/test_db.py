import db
import sqlite3


def test_create_admininfo_table():
    connection = db.create_connection()

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


def test_create_bookinginfo_table():
    connection = db.create_connection()

    db.create_bookinginfo_table(connection)

    connection.execute(
        "INSERT INTO BookingInfo(name, email, topic) values ('Elon Musk', 'elon_musk@spacex.com', 'contract negotiation')"
    )
    connection.execute(
        "INSERT INTO BookingInfo(name, email, topic) values ('Maye Musk', 'me@mayemusk.com', 'The presentation of the new book')"
    )
    cursor = connection.execute("SELECT * FROM BookingInfo")
    result = cursor.fetchall()
    assert len(result) == 2
    assert result[0] == (
        1, 'Elon Musk', 'elon_musk@spacex.com', 'contract negotiation')
    assert result[1] == (2, 'Maye Musk', 'me@mayemusk.com',
                         'The presentation of the new book')

    connection.close()


def test_create_slots_table():
    connection = db.create_connection()
    db.create_bookinginfo_table(connection)
    db.create_slots_table(connection)

    connection.execute(
        "INSERT INTO BookingInfo(name, email, topic) values ('Elon Musk', 'elon_musk@spacex.com', 'contract negotiation')"
    )

    booking_id = connection.execute("SELECT id FROM BookingInfo").fetchone()[0]

    connection.execute("INSERT INTO slots(start_date, booking_id) values(?, ?)",
                       ('2021-09-01 12:00:00', booking_id))
    connection.execute("INSERT INTO slots(start_date, booking_id) values(?, ?)",
                       ('2021-09-01 12:15:00', booking_id))

    result = connection.execute("SELECT * FROM slots").fetchall()
    assert len(result) == 2
    assert result[0] == (1, '2021-09-01 12:00:00', 1)
    assert result[1] == (2, '2021-09-01 12:15:00', 1)

    connection.close()
