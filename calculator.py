from ast import Num


def add(a,b):
    answer=a+b
    return answer

def substract(a,b):
    answer=a-b
    return answer

def multiply(a,b):
    answer=a*b
    return answer

def divide(a,b):
    answer=a/b
    return answer

def modulus(a,b):
    answer=a%b
    return answer
    
def exponent(a,b):
    answer=a**b
    return answer

def int_divide(a,b):
    answer=a//b
    return answer

def square(a):
    answer=a*a
    return answer

def cube(a):
    answer=a**3
    return answer

# num = int(input("enter a number: "))
# fac = 1
# for i in range(1, num + 1):
#  fac*=1
# print("factorial of ", num, " is ", fac)

def factorial(number):
    factor=1
    for i in range(1, number + 1):
        factor*=1
    return factor    
    
    
    
    
    
    
    