"""Algorithms in school assignment two."""
import time

# GENERATORS 1. Write a generator function that gives you the next number in the Fibonacci sequence


def gen_fib():
    """Fibonacci using generator."""
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b


fib_gen = gen_fib()

print(next(fib_gen))
print(next(fib_gen))
print(next(fib_gen))
print(next(fib_gen))

# COMPREHENSIONS 1. Write a function that takes in a list of strings and returns every character in those strings.


def sep_char_list(a_list: list) -> list:
    """Take a list of string and return every character in those strings."""
    new_list = [[c for c in word] for word in a_list]
    return new_list


print(sep_char_list(['apple', 'pear', 'banana', 'cherry']))

# DICT 1. Write a function (that uses reduce) that converts the following dict:

tha_dict = {"john": {"age": 32, "favourite_color": "pink"},
            "sarah": {"age": 22, "favourite_color": "red"},
            "hannah": {"age": 19, "favourite_color": "green"},
            "michael": {"age": 56, "favourite_color": "blue"},
            "david": {"age": 43, "favourite_color": "yellow"}}


def convert_dict(result_list: list, a_dict: dict) -> list:
    """Take the dict 'tha_dict' and return a list of dicts with new key['name'] and value."""
    result_list = result_list
    for k, v in a_dict.items():
        name = k
        v['name'] = name
        result_list.append(v)
        result_list = sorted(result_list, key=lambda kv: kv['age'])
    return result_list


print(convert_dict([], tha_dict))

# Decorators 1. Write a decorator called lower cased that can be used to turn any result of a function
# returning a string into lowercase.


def lower_cased(func):
    """Return string into lowercase."""
    def wrapper(name: str) -> str:
        word = func(name)
        return word.lower()
    return wrapper


# 2. Write a decorator called tired that makes a function sleep before returning its result.

def tired(n: int):
    """Sleep n number of seconds."""
    def decorator(func):
        def wrapper(name: str) -> str:
            time.sleep(n)
            return func(name)
        return wrapper
    return decorator


@tired(3)
@lower_cased
def get_name(name: str) -> str:
    """Return name with decorators @tired and @lowercase."""
    return name


print(get_name('John Doe'))


# Lambda 1. Use a lambda and the built-in function function filter to filter out all numbers greater
# than 42 in the following list: [60, 91, 38, 13, 18, 34, 15, 74]

print(list(filter(lambda x: x > 42, [60, 91, 38, 13, 18, 34, 15, 74])))

