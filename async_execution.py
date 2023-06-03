from collections import deque
import heapq
import time


def get_page():
    print("Start downloading page")
    yield "sleep", 1
    print("Successed")
    yield "<html>Hello!</html>"


def read_db():
    print("Start retrieve data from db")
    yield "sleep", 1 ## запрос на сервер
    print("Connected")
    yield "sleep", 0.5
    print("Retrieved")
    yield "db_data"


def run():
    start = time.time()
    get_page()
    read_db()
    print(f"Elapsed time = {time.time() - start:.3}")


def scheduler(coros):
    start = time.time()
    ready = deque(coros)
    sleeping = []

    while True:
        if not ready and not sleeping:
            break
        if not ready:  # Ожидаю готовности к выполнению корутины
            deadtime, coro = heapq.heappop(sleeping)
            if deadtime > time.time():
                time.sleep(deadtime - time.time())
            ready.append(coro)
        try:
            coro = ready.popleft()
            result = coro.send(None)
            if len(result) == 2 and result[0] == "sleep":
                deadtime = time.time() + result[1]
                heapq.heappush(sleeping, (deadtime, coro))
            else:
                print(f"Получен результат: {result}")
                ready.append(coro)
        except StopIteration:
            pass
    print(f"Elapsed time = {time.time() - start:.3}")


# scheduler((get_page(), read_db()))
