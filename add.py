def upper_lower(x):
    upper = x.upper() # Convert x to upper string
    lower = x.lower() # Convert x to lower string
    return upper, lower # Return both variables


upper, lower = upper_lower('Python')
print(upper)
print(lower)

