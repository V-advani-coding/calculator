def sum(a, b):
    total = a+b
    print("sum of 2 numbers is  ", total)


def difference(a, b):
    diff = a-b
    print("difference of 2 numbers is  ", diff)

def divide(a, b):
    div = a/b
    print("divide of 2 numbers is  ", div)


def multiply(a, b):
    multi = a*b
    print("multiply of 2 numbers is  ", multi)

number1=int(input("give first number"))
number2=int(input("give second number"))

sum(number1,number2)
difference(number1,number2)
multiply(number1,number2)
divide(number1,number2)