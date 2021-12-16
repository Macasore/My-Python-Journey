def picnicitem(itemdict, leftwidth, rightwidth ):
    print('PICNIC ITEMS'.center(leftwidth+rightwidth, '-'))
    for k,v in itemdict.items():
        print(k.ljust(leftwidth, '-') +str(v).rjust(rightwidth, '-'))
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
picnicitem(picnicItems, 12, 5)
