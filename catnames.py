catnames = []
while True:
    print('Enter the name of cat' +str(len(catnames) + 1)+ ' ( or enter nothing to break.):')
    name = input()
    if name == '':
        break
    catnames = catnames + [name]

print('the names of your cats are:')
for name in catnames:
    print(name)
