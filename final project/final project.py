#TASK 4:
attempts = 0 # number of attempts
valid_username = 'Amine'
valid_password = '123'
Login = 0 #Login status
while attempts < 3:
    username = input("Write your username: ") #asking for username
    password = input("Write your password: ") #asking for password
    if username != valid_username and password != valid_password:
        print("Wrong information")
        attempts +=1 #adding attempts
    elif username == valid_username and password == valid_password:
        print("Login succesfull")
        Login = True #Login is true
        break
if attempts == 3:
    print("too many attempts")
    Login = False #login unsuccesfull

menu = 0 #menu options
def Temperature_ranges (temp): #see where the temperature falls
    if temp <10: #temp has to be no bigger than 10
        weather = 'cold'
        return weather
    if temp > 9 and temp < 20: #temp has to be between 10 and 19
        weather = 'mild'
        return weather
    if temp > 19: #temp has to be bigger than 19
        weather = 'warm'
        return weather
def clothing_suggestion (weather, rain, wind): #clothing suggestions
    if weather  == 'cold':
        print("Bring a heavy coat")
    elif weather == 'mild':
        print('Bring light layers')
    elif weather == 'warm':
        print('Bring a t-shirt and shorts')
    if rain == 'yes':
        print('Bring an umbrella')
    if wind == 'yes':
        print('Bring wind resistant clothes')
inputed = 0 #seeing if user inputed weather info

while Login == True and menu !=3: #Login has to be true to get access
    menu = int(input('Choose the following options: \n1:Enter todays weather \n2:Get clothing suggestion \n3:Exit\n'))
    if menu == 1: #Choice 1
        #asking for input
        temperature_in_celsius = int(input('Enter temperature in Celsius: '))
        while temperature_in_celsius > 50 or temperature_in_celsius < -40:
            print("enter a valid value")
            temperature_in_celsius = int(input('Enter temperature in Celsius: '))
        raining_status = input("is it raining?: ")
        while raining_status != 'yes' and raining_status != 'no': #ensuring right values
            print("enter a valid value")
            raining_status = input("is it raining?: ")
        wind_status = input("is it windy?: ")
        while wind_status != 'yes' and wind_status != 'no': #ensuring right values
            print("enter a valid value")
            wind_status = input("is it raining?: ")
        inputed = 1 #the user has inputed weather info
    elif menu ==2 and inputed ==1: #Choice 2 and making sure that weather
        clothing_suggestion(Temperature_ranges(temperature_in_celsius),raining_status,wind_status )
