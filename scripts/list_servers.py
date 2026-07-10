from app.database.session import SessionLocal
from app.database.models import Server

db = SessionLocal()

servers = db.query(Server).all()

for server in servers:
    print(
        server.id,
        server.name,
        server.ip_address,
        server.operating_system,
        server.status,
    )

db.close()
