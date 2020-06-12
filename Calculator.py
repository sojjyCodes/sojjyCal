#Created by sojjyCodes
#! usr/bin/python3
while True:
    try:
        operation = int(input('''
        What task do you wish to perform:
        1 for Addition
        2 for Substraction
        3 for Multiplication
        4 for Division
        '''))

        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number:'))

        if operation == '1':
            print('{} + {} = '.format(number_1, number_2))
            print (number_1 + number_2)

    #Substraction
        elif operation == '2':
            print('{} - {} = '.format(number_1, number_2))
            print (number_1 - number_2)

        #Multiplication
        elif operation == '3':
            print('{} * {} ='.format(number_1, number_2))
            print (number_1 * number_2)

        #Division
        elif operation == '4':
            print('{} / {}'.format(number_1, number_2))
            print (number_1 / number_2)

    except NameError:
        print("Error occured when receiving input. Try again!")
