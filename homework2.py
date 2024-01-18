# Task 1

# If the temperature is 25 Celsius, convert to Fahrenheit and Kelvin.

num_c = float(25)
converter_to_fahrenheit = (num_c * 9 / 5) + 32
converter_to_kelvin = num_c + 273.15
print(converter_to_fahrenheit)
print(converter_to_kelvin)

# the task of converting from degrees Celsius to degrees Fahrenheit with input

num_for_celsius_f = float(input('Enter the number in Celsius to convert to Fahrenheit: '))
converter_celsius_to_fahrenheit = (num_for_celsius_f * 9 / 5) + 32
print(converter_celsius_to_fahrenheit)

# the task of converting from degrees Celsius to degrees Kelvin  with input

num_for_celsius_k = float(input('Enter the number in Celsius to convert to Kelvin: '))
converter_celsius_to_kelvin = num_for_celsius_k + 273.15
print(converter_celsius_to_kelvin)

# Task 2 if we use only 'if' and  'else'

operation = input("Enter operation: '+', '-', '*', '/', '//', '%' '**', 'Exit': ")
num_1 = float(input('Enter first numb:'))
num_2 = float(input('Enter second numb:'))

if operation == '+':
    result = (num_1 + num_2)
    print(result)

if operation == '-':
    result = num_1 - num_2
    print(result)

if operation == '*':
    result = num_1 * num_2
    print(result)

if operation == '/':
    if num_2 != 0:
        result = num_1 / num_2
        print(result)
    else:
        print("Error: Division by zero")

if operation == '//':
    result = num_1 // num_2
    print(result)

if operation == '%':
    result = num_1 % num_2
    print(result)

if operation == '**':
    result = num_1 ** num_2
    print(result)

if operation == 'Exit':
    print('program completed')


