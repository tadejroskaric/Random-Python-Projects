import random

# A simple password generator with 2 capital and 2 small letters, 2 numbers and 2 additional signs

capital_letter1 = chr(random.randint(65, 90))
capital_letter2 = chr(random.randint(65, 90))

small_letter1 = chr(random.randint(97, 122))
small_letter2 = chr(random.randint(97, 122))

number1 = chr(random.randint(48, 57))
number2 = chr(random.randint(48, 57))

sign1 = chr(random.randint(32, 64))
sign2 = chr(random.randint(32, 64))

password = capital_letter1 + capital_letter2 + small_letter1 + small_letter2 + number1 + number2 + sign1 + sign2

print(password)
