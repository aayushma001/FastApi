from app.core.database import Base, engine
from app.db.models import user

def create_tables():
    Base.metadate.create_all(bind=engine)