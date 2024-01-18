# Task 2 with Cycle

while True:
    operation = input("Enter operation 2.0: '+', '-', '*', '/', '//', '%' '**', 'Exit': ")

    if operation == 'Exit':
        print('Program completed.')
        break

    Num_1 = float(input('Enter first numb:'))
    Num_2 = float(input('Enter second numb:'))

    if operation == '+':
        result_2 = Num_1 + Num_2

    elif operation == '-':
        result_2 = Num_1 - Num_2

    elif operation == '*':
        result_2 = Num_1 * Num_2

    elif operation == '/':
        if Num_2 != 0:
            result_2 = Num_1 / Num_2
        else:
            print("Error: Division by zero")
            continue

    elif operation == '//':
        result_2 = Num_1 // Num_2

    elif operation == '%':
        result_2 = Num_1 % Num_2

    elif operation == '**':
        result_2 = Num_1 ** Num_2

    else:
        print("Invalid operation. Please enter a valid operation.")
        continue

    print("Result:", result_2)
