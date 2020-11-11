def add(m,n):
    if n == 0:
        return m
    else:
        return add(m,n-1) + 1

def mult(m,n):
    if n == 0:
        m=0
        return m  
    else:
        return add(m,mult(m,n-1))

def power(m,n):
    if n == 0:
        return 1
    else:
        return mult(m,power(m,n-1))

print(add(5,3))
print(mult(8,3))
print(power(6,3))