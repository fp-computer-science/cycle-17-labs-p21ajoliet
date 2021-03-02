#Author: ALJ (AMDG) 3/1/21

def factorial(number):
    if number == 0:
        return 1
    else:
        recurse = factorial(number - 1)
        result = number * recurse
        return result

result = factorial(3)
print(result)