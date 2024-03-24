from database.utils.outbase import outbaseInterface
from database.common.models import db, History
from datetime import datetime

class outbaseInterface():
    @staticmethod
    def create(db, data):
        return History.create(timestamp=datetime.now(), user_id=data['user_id'], command=data['command'])
db.connect()
db.create_tables([History])

outbase = outbaseInterface()

if __name__ == "main":
    outbase()