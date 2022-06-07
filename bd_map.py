import sqlite3
from config import bot


def sql_create():
    global connection, cursor
    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()
    if connection:
        print("Database connected successfully")
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS news
        (image TEXT, title TEXT PRIMARY KEY, link TEXT)
        """
    )
    connection.commit()


async def sql_insert(state):
    async with state.proxy() as data:
        cursor.execute(
            """
        INSERT INTO news VALUES (?, ?, ?)
        """,
            tuple(data.values()),
        )

        connection.commit()


async def sql_select(message):
    for result in cursor.execute("""SELECT * FROM news""").fetchall():
        await bot.send_photo(
            message.chat.id,
            result[0],
            caption=f"Title {result[1]}\n" f"Link: {result[2]}",
        )


async def sql_delete(data):
    cursor.execute(
        """
    DELETE FROM media WHERE title == ?
    """,
        (data,),
    )
    connection.commit()
