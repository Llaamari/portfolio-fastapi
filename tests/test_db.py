from app.db.session import engine


def test_database_connection():
    connection = engine.connect()
    connection.close()