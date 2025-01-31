import os

from motor.motor_asyncio import AsyncIOMotorClient

DATABASE_NAME = os.environ.get("MONGO_DATABASE", "yorigin")

client = AsyncIOMotorClient()
db = client[DATABASE_NAME]

import asyncio


# Added -> None
async def print_mongo_version() -> None:
    status = await client.test.command("serverStatus")
    print(status["version"])


asyncio.run(print_mongo_version())
