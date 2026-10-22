def greet():
    name = input("Write your name : ")
    print("Hello , ", name)


# if you are not returtning something, its goign to return None.


def say_vanakam(name):
    return "Vanakam, " + name


def celsius_to_farenheit(celsius):
    farenheit = (celsius * 1.8) + 32
    return farenheit


def lets_say_hi_to_students(*args):
    print(args, type(args))
    for name in args:
        print("Hi ", name)


lets_say_hi_to_students("Syed", "Jafer", "Wijay", "Karthik", "Dinesh", "Siva")

# greet()
# response = say_vanakam(name="Jafer")
# print(response)

# response = celsius_to_farenheit(24)
# print(response)
