def find_factorial(n):
    if n==1:
        return n
    else:
        return n*find_factorial(n-1)
num=find_factorial(5)
print(num)