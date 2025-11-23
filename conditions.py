x=input('Enter Your Password : ')

if(x=='123'):
    print('you are successfully authenticated')
elif(len(x) > 3):
    print("Password is of 3 digits.")
elif(len(x) < 3):
    print("Password is of 3 digits.")
else:
    print('Incorrect Password, Try Again')
