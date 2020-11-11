def convert2fahren(celstemp):
    '''
    Return the temperature in fahrenheit given the temperature in celsius, celstemp.
    '''
    fahrentemp = celstemp*(9/5)+32
    return fahrentemp
print("0 ->",convert2fahren(0))
print("32 ->",convert2fahren(32))
print("100 ->",convert2fahren(100))