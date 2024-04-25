while True:
    user_input1 = int(input("Enter the First Value: "))
    user_input2 = int(input("Enter the Second Value: "))
    op_input = input("Please Select Any of the Following\n+\n-\n*\n/: ")
    if op_input == "+":
        ans1 = user_input1 + user_input2
        print(ans1)
    elif op_input == "-":
        ans2 = user_input1 - user_input2
        print(ans2)
    elif op_input == "*":
        ans3 = user_input1 * user_input2
        print(ans3)
    elif op_input == "/":
        ans4 = user_input1 / user_input2
        print(ans4)
    else:
        print("Invalid Input")

    another_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() != 'yes':
        break
