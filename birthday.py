birthdays = {'blessing': 'march 3', 'isaac': 'january 27', 'queen esther': 'march 13', 'david': 'september 2'}

while True:
    print('enter name of person to get birthday (or leave blank to quit) ')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name]+ ' is the birthday of ' +name)
    else:
        print('sorry we do not have that name on our database')
        print('enter the birthday of the name')
        bday = input()
        birthdays[name] = bday
        print('birthday updated')
        