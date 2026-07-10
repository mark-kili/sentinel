from app.database.base import Base
from app.database.engine import engine

import app.database.models

Base.metadata.create_all(bind=engine)

print("Database created successfully!")
