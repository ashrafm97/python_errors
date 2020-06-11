while True:
    try:
        user_input = int(input("Enter any no. to continue:  "))
    except ValueError:
        print("Input must be a number! Try again  ")
    else:
        print("Thank you. ")
        break