from database import Engine, Base
import model

Base.metadata.create_all(bind=engine)