def greet(name):
    print(f"Hi there {name}")
    print("Welcome aboard")


def get_greeting(name):
    return f"Hi {name}"


# message = get_greeting("Francis")
# file = open("content.txt", "w")
# file.write(message)

# def increment(number, by=1):
#     return number + by


# print(increment(2, 2))


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))
