def decor(func):
    def inner1(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except ZeroDivisionError as e:
            print(f"A Zero Division Error Occurred {e}") 
        except TypeError as e:
            print(f"TypeError: Both inputs should have a numeric values {e}")
        except IOError as e:
            print(f"As IOError occurred {e}")
        except EOFError as e:
            print(f"As EOFError occurred {e}")
    return inner1

# Write a Python program that takes two integers as input and performs division (num1 / num2). 
# Handle the ZeroDivisionError and display a custom error message when the second number is zero.

@decor
def divide(numerator,denominator):
    print(numerator/denominator)
    
divide(6,2)

# Implement a program that takes user input for a filename, opens the file in read mode, and displays its contents. 
# Handle the FileNotFoundError and display an error message if the file is not found.


@decor
def file_display(filename):
    file = open(filename,"r")
    for line in file:
        print(line)
    file.close()


file_display('file.txt')

# Write a Python program that takes a user input and converts it to an integer. 
# Handle the ValueError and display a custom error message when the input cannot be converted to an integer.

try:
    uinput = int(input("Enter a number: "))
except ValueError as e:
    print("ValueError: Please provide a valid number ",e)


# Write a Python program that takes user input for age. 
# Create a custom exception InvalidAgeError to handle cases where the age is below 0 or above 120.

class InvalidAgError(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age<0 or age >120:
        raise InvalidAgError
    
except TypeError as e:
    print("Enter a proper numeric value")
except InvalidAgError as e:
    print("Please Enter values between 0 and 120")
    


# Implement a program that reads user input for a password. 
#Create a custom exception WeakPasswordError to handle cases where the password is shorter than 8 characters.
    
class WeakPasswordError(Exception):
    def __init__(self, password):
        self.password = password
        self.message = "Input Password Longer than 8 characters: "+"'"+self.password+"' "+"Too Weak"
        super().__init__(self.message)

try:
    password = input("Enter your password: ")
    if len(password)<8:
        raise WeakPasswordError(password)
except WeakPasswordError as e:
    print(e)






