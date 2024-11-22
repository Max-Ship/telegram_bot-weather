from database.comands import Commands
from database.model import db, History

db.connect()
db.create_tables([History])

commands_db = Commands()

if __name__ == '__main__':
    commands_db()
