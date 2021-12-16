import copy
cat = ['black', 'small', 'male']
colour, size, gender = cat 
print(size)
man = cat.index('black')
print(man)
family = ['david', 'maca', 'isaac', 'queen esther']
family.append('mysley')
family.insert(2, 'susannah' )
family.remove('david')
family.sort(reverse = True)
print(family)
def eggs(Someparameter):
    Someparameter.append('hello')
spam = [1,2,3]
eggs(spam)
print(spam)
sperm = [[1,2,3,4,5],[6,7,8,9,10]]
cheese = copy.copy(sperm)
cheese[1] = 'hello'
print(sperm)
print(cheese)