from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient('mongodb://mongodb:27017')
db = client.get_database("btg_db")

