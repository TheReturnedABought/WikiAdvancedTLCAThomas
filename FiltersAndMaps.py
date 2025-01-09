
numbers = [1, 2, 3, 4, 5, 6]

# Filter out even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Square each number using map
squared_numbers = list(map(lambda x: x**2, numbers))

print("Even numbers:", even_numbers)
print("Squared numbers:", squared_numbers)