from asyncio import sleep
import asyncio


async def get_page():
    print("Start downloading page")
    await sleep(1)
    print("Successed")
    return "<html>Hello!</html>"


async def write_db(data):
    print("Start retrieve data from db")
    await sleep(1)
    print("Connected")
    await sleep(0.5)
    print("Retrieved")
    return "db_data"


async def worker():
    page = await get_page()
    await write_db(page)


async def main():
    workers = await asyncio.gather(worker(), worker())


asyncio.run(main())
