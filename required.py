while True:
    print('enter your age')
    age = input()
    if age.isdecimal():
        break
    print('enter a numerical value')

while True:
    print('select a new password(letters and numbers only)')
    password = input()
    if password.isalnum():
        break
    print('passwords can only have letters and numbers')

