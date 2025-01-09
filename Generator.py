# A generator to yield even numbers up to n
def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i  # Yield values one by one

# Use the generator
for num in even_numbers(10):
    print(num)