def xo(s):
    figure = s
    first = figure.count('x')
    second = figure.count('o')
    if first == second:
        return True
    else:
        return False         
xo('xo')
xo('xo0')
not xo('xxxoo')

        
   