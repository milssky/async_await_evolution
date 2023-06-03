# .send()
# .throw()
# .close()

def coro():
    while True:
        value = yield
        print(f"Полученное значение - {value}")


def maximum():
    max_num = None
    while True:
        n = yield max_num
        max_num = n if max_num is None or n > max_num else max_num

print()