# Use lambda to sort a list of dictionaries by age
people = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 20}, {"name": "Eve", "age": 30}]

# Sort by 'age' using lambda
sorted_people = sorted(people, key=lambda person: person['age'])

print(sorted_people)