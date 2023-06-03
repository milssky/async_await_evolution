from async_execution import scheduler

def get_page():
    print("Start downloading page")
    yield "sleep", 1
    print("Successed")
    yield "<html>Hello!</html>"


def write_db(data):
    print("Start retrieve data from db")
    yield "sleep", 1
    print("Connected")
    yield "sleep", 0.5
    print("Retrieved")
    yield "db_data"


def worker():
    page = yield from get_page()
    yield from write_db(page)


scheduler([worker(), worker(), worker()])
