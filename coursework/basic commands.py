#Creating 3 variables:
A = int(3) #Intger value
B = float(4.17) #floating-point number
C = str("Hello") #string value

print(A, B, C)

#Age has an integer value:
age = 18
#Printing the type
print(type(age))
#changing the variable:
age = 18.5
print(type(age))

#declaring the variable is_student
is_student = True
#printing the type:
print(type(is_student))

#asking user for name
user_name = input("Write your name: ")
#printing a message:
print(f'Hello, {user_name}!')
# asking for age
user_age = int(input("Write your age: "))
#condition if the user is old enough
if user_age >= 18: #if user is 18 or older
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

#asking for a number as string
user_number = str(input("Enter a number: "))
# converting into an integer
user_number = int(user_number)
#printing squared value of the integer
print(user_number**2)

#string representing a float number:
value = str(4.56)
#conversion
value = float(value)
print(value * 2) #printing result

#addition:
a = 45 + 67
#substraction:
a = 156 - 89
#multiplication:
a = 12 * 7
#division
a = 100/4
#finding remainder
a = 10%3
#raising power:
a = 3**4

#comparison:
a = 10
b = 20
# printing results of comparison:
print(a==b)
print(a!=b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)

#Asking user for a number
num = input("Enter your first number: ")
num1 = input("Enter the second number: ")
if num > num1: #comparison
    print("First number is greater than the second number")
elif num == num1:
    print("First number is equal to the second number")
else:
    print("First number is smaller than the second number")

#Asking user for number:
number = int(input("Enter a number: "))
if number > 10 and number < 20: #Seeing if num is greater than 10 and less than 20
    print("Your number is between 10 and 20")
else:
    print("Your number is not between 10 and 20")

if number < 5 or number > 50: #Seeing if number is either less than 5 or greater than 50
    print("Your number is not between 5 and 50")
else:
    print("Your number is between 5 and 50")

age = int(input("Enter your age: "))  # Ask the user for their age
if age >= 18:
    print("You are an adult.")  # If age is 18 or more
else:
    print("You are a minor.")  # If age is less than 18

number = int(input("Enter a number: "))  # Ask the user for a number
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")  # Divisible by both 3 and 5
elif number % 3 == 0:
    print("Fizz")  # Divisible by 3 only
elif number % 5 == 0:
    print("Buzz")  # Divisible by 5 only
else:
    print(number)  # Not divisible by 3 or 5

for i in range(1, 11):  # range(start, stop) - stop is exclusive, so we use 11
    print(i)

i = 2
while i <= 20:  # Loop continues as long as i is less than or equal to 20
    print(i)
    i += 2  # Increase i by 2 to stay on even numbers

n = int(input("Enter a number n: "))  # Ask the user for input
print(f"Numbers from 1 to {n} that are divisible by 4:")
for i in range(1, n + 1):  # Loop from 1 to n (inclusive)
    if i % 4 == 0:  # Check if i is divisible by 4
        print(i)

