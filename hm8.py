def two():
    exponent = 0
    while True:
        yield 2 ** exponent
        exponent += 1


iterator = iter(two())

for _ in range(10):
    print(next(iterator))

for _ in range(5):
    print(next(iterator))