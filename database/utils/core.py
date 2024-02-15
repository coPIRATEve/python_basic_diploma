from database.utils.outbase import outbaseInterface
from database.common.models import db, History

db.connect()
db.create_tables([History])

outbase = outbaseInterface()

if __name__ == "main":
    outbase()