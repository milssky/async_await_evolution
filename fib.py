def fibonacci_list(n):
    a, b = 1, 1
    numbers = []
    for _ in range(n):
        numbers.append(a)
        a, b = b, a + b
    return numbers


# print(fibonacci_list(10000000))

# 1 1 2 3 5 8 13 ...

def fibonacci_generator(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


class Finnonacci:
    def __init__(self, n):
        self.a, self.b = 1, 1
        self.n = n
        self.i = 0

    def __next__(self):
        if self.i == 0:
            self.i += 1
            return self.a
        elif self.i < self.n:
            self.a, self.b = self.b, self.a + self.b
            self.i += 1
            return self.a
        else:
            raise StopIteration

    def __iter__(self):
        return self


for number in Finnonacci(10):
    print(number)