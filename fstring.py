first_name = input("what is your first name : ")
last_name = input("what is your last name : ")
username = first_name+'.'+last_name
print(f"your User name is {username}")



# Define a username and password
stored_password = "1234"

# Prompt the user for input

COUNT = 0
while (COUNT<=2):
    entered_password = input("Enter your password: ")
    if entered_password == stored_password:
        print('you are successfully authenticated')
        break
    else:
        print('Incorrect Password, Try Again')
    COUNT += 1

for i in range(3):
    entered_password = input("Enter your password: ")

    if entered_password == stored_password:
        print('you are successfully authenticated')
        break
    else:
        print('Incorrect Password, Try Again')

print('calculator')

num_1 =int(input('Please, enter the first number:'))
num_2 =int(input('Please, enter the second number:'))
add =  num_1+num_2
# operation : Addition
print('Addition of {} + {} = {}'.format(num_1, num_2,add))

print(f'Addition of {num_1} +{num_2} = {add}')

