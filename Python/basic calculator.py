q1 = input("would you like to 1.Addition, 2.Substraction, 3.Multiplication: ")
q1 = int(q1)

if q1 == 1:
    first_number = input("enter a number for addition: ")

    second_number = input ("enter a second number: ")

    result = int(first_number)+ int(second_number)


    print(result)



elif q1 == 2:
    first_number = input("enter a number for substraction: ")

    second_number = input ("enter a second number: ")

    result = int(first_number) - int(second_number)


    print(result)




elif q1 == 3:
    first_number = input("enter a number for Multiplication: ")

    second_number = input ("enter a second number: ")

    result = int(first_number) * int(second_number)


    print(result)



else:
    print("Please use the valid options (either 1, 2 or 3). ")
    
