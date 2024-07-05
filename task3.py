import random

upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_case = 'abcdefghijklmnopqrstuvwxyz'
symbol_s = '[]{}()!@#$%^&*'
digit_s = '1234567890'

all = upper_case + lower_case + symbol_s + digit_s
print("WELCOME TO PASSWORD GENERATOR.....")

length = int(input("enter the length of the password: "))

upper = int(input("enter the number of upper case letters: "))
lower = int(input("enter the number of lower case letters: "))
symbol = int(input("enter the number of symbols: "))
digit = int(input("enter the number of digits: "))

add = random.choices(upper_case,k=upper) + random.choices(lower_case,k=lower) + random.choices(symbol_s,k=symbol) + random.choices(digit_s,k=digit)

password = "".join(random.sample(add,length))
print("password generator is",password)

