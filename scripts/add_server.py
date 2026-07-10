from app.database.session import SessionLocal
from app.database.models import Server

db = SessionLocal()

server = Server(
    name="Home Server",
    ip_address="192.168.1.100",
    operating_system="Ubuntu 24.04",
    status="online",
)

db.add(server)
db.commit()

print("Server added!")

db.close()
