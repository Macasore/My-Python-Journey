spam = "this is alice's cat"
#escape characters
#for using quotation mark in a single quote
maca = 'this is maca\'s example'
print(maca)
examples = 'i don\"t \nknow\t guy' 
# \t = tab
# \n = new line
print('''Dear alice,
it's maca and im trying this triple quotation mark thingy let's see if it works.
sincerly,
maca''')
print(examples)
# r -makes it raw(print it exactly how it is )
print(r'I\'m a boy')

""" This is a multi line comment section basically what we have been seeing regularly
i guess """
print('hello how your day?')
feeling = input()
if feeling.lower() == 'great':
    print('mine was great too')
else:
    print('i hope you enjoy the rest of it')
# feeling.isupper() or .islower()---- is used to check if it's upper or lower
# .isalpha(checking for only letters)
# .isalnum(checking for only letters and numbers)
# .isdecimal(checking for only numerical values)
# . isspace(checking for space, tab and newlines)
# .istitle(checking for words that starts with only uppercase and are followed by lowercase members)
# ' '.join(['cats', 'rats', 'dogs'])  - to concatenate 
# 'my name is simon'.split()-- does the opposite of join
# 'myabcnameabcisabcdavid'.split('abc')
# rjust() and ljust() are for filling the spaces in a string to either the left or right
# there is also.center()
# strip()-- to remove white space
#lstrip(), rstrip()

