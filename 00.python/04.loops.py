# num = int(input("Enter the number"))

# start = 0
# end = num

# for n in range(start, end):
#     if n % 2 == 0:
#         print("Fizz")
#     elif n % 3 == 0:
#         print("Buzz")
#     elif n % 2 == 0 and n % 3 == 0:
#         print("FizzBuzz")
#     else:
#         print(n)


# for n in range(start, end + 1):
#     if n % 2 == 0 and n % 3 == 0:
#         print("FizzBuzz")
#     elif n % 2 == 0:
#         print("Fizz")
#     elif n % 3 == 0:
#         print("Buzz")
#     else:
#         print(n)


# def fizz_buzz(num):
#     match num:
#         case 200:
#             return "OK"
#         case 500 | 502 | 503:
#             return "Server Error"
#         case num if num % 2 == 0 and num % 3 == 0:
#             return "FizzBuzz"
#         case num if num % 2 == 0:
#             return "Fizz"
#         case num if num % 3 == 0:
#             return "Buzz"
#         case _:
#             return num


# for n in range(start, end + 1):
#     res = fizz_buzz(n)
#     print(res)


num = -10
while num:
    print(num)  # Logic
    num = num + 1  # which decides the break

x = -1
match x:
    case _ if x:
        print("True Value")
    case _:
        print("False Value")
