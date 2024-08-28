#recursive algorithm
def factorial(n):
    if n==1 or n==0:
        return n
    else:
        return n*factorial(n-1)
    
n= int(input("enter the number you want to find a factorial for: "))
print(factorial(n))
