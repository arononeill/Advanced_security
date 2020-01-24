import random
  
# Function to implement a modular exponentiation, returning (x^y) % z
def power_function(x, y, z):
    result = 1

    # Gets the modular of x if its more than or equal to z
    x = x % z
    while y > 0:
          
        # multiply result and x if y is odd
        if y & 1:
            result = (result * x) % z
  
        # y will be even here
        y = y >> 1
        x = (x * x) % z
      
    return result
  
# This function is implemented however long the number of iterations is set to.
# It returns True if input_number is composite and returns false if input_number is probably prime.
# Odd_number is an odd number such that odd_number*2<sup>r</sup> = input_number-1 for some r >= 1
def miillerTest(odd_number, input_number):
      
    # Generates a random number in [2..input_number-2] Corner cases whilst ensuring input_number > 4
    a = 2 + random.randint(1, input_number - 4)
  
    # call power_function, passing the appropriate parameters
    x = power_function(a, odd_number, input_number)
  
    if x == 1 or x == input_number - 1:
        return True
  
    # Keep squaring x while the odd_number fails to reach input_number-1, (x^2) % input_number is not 1
    # or (x^2) % input_number is not input_number-1
    while odd_number != input_number - 1:
        x = (x * x) % input_number
        odd_number *= 2
  
        if x == 1:
            return False
        if x == input_number - 1:
            return True

    return False


""" This function returns false if input_number is composite and returns true if input_number is probably prime.
    iterations_length is the number of iterations that determines accuracy level. Higher value of.
    Accuracy increases as iterations_length does """
def isPrime(n, iterations_length):

    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True

    odd_number = n - 1
    while odd_number % 2 == 0:
        odd_number //= 2
  
    # Iterate through using the given number of 'iterations_length'
    for i in range(iterations_length):
        if not miillerTest(odd_number, n):
            return False
  
    return True
  

iterations_length = 40
choice = 1
# User display enabling them to enter a prime number for checking
while choice == 1:
    print("Press 1 to check if a number is prime"
          "\nPress 3 to exit\n")
    choice = input("Choice: ")
    choice = int(choice)
    print(choice)
    if choice == 1:
        print("Please enter a number to check if its prime\n")
        number_check = input("Choice: ")
        check = number_check.isdigit()

        if check:
            n = int(number_check)
            if isPrime(n, iterations_length):
                print(n, "is prime\n")

            else:
                print(n, "is 'composite'\n")

        else:
            print("\nPlease enter a value numeric value when searching for a prime number\n")

    elif choice == 3:
        print("\n\t Thank you for using this service\n")

    else:
        print("Please enter a valid choice!")
