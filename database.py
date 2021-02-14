import motor.motor_asyncio

from config import DATABASE_URL

client_db = motor.motor_asyncio.AsyncIOMotorClient(
    DATABASE_URL, uuidRepresentation="standard"
)
db = client_db["test"]
collection = db["users"]