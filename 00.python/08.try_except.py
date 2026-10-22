def divide(num_a, num_b):
    try:
        response = num_a / num_b
        raise Exception("Test Exception")
        return response
    except ZeroDivisionError:
        print("Cant divide by zero")
    except Exception as ex:
        print(str(ex))


print(divide(4, 2))
print(divide(2, 4))
print(divide(3, 1))
