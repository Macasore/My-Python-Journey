def spam(divideby):
    try:
        return 42/divideby
    except ZeroDivisionError:
        print('ERROR: Invalid argument.')

print(spam(2))
print(spam(1))
print(spam(0))


