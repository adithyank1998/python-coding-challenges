def smart_number_analyzer():
    user_input = input("Enter a number: ")

    # Input validation
    try:
        number = int(user_input)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        return

    # Check Even or Odd
    if number % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

    # Check Positive, Negative, or Zero
    if number > 0:
        print("Positive Number")
    elif number < 0:
        print("Negative Number")
    else:
        print("Zero")

    # Sum of Digits (Using Loop)
    temp = number

    # Handle negative numbers
    if temp < 0:
        temp = -temp

    digit_sum = 0

    while temp > 0:
        digit = temp % 10
        digit_sum = digit_sum + digit
        temp = temp // 10

    print("Sum of digits:", digit_sum)


# Run Program
smart_number_analyzer()