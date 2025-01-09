
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper


def say_hi():
    return 'hello there'

decorate = uppercase_decorator(say_hi)
print(decorate())

#However, Python provides a much easier way for us to apply decorators.
# We simply use the @ symbol before the function we'd like to decorate.
# Source: https://www.datacamp.com/tutorial/decorators-python