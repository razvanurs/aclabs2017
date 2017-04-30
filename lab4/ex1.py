#! python3
class Fibonacci(object):
    def __init__(self, n):
        self.previous = 0
        self.current = 1
        self.limit = n

    def __iter__(self):
        return self

    def __next__(self):
        fib = self.current
        if fib > self.limit:
            raise StopIteration
        self.current += self.previous
        self.previous = fib
        return fib


for num in Fibonacci(100):
    print(num, end=' ')
