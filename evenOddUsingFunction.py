# WAP to find out even/odd using functions

n = int(input("Enter a number : "))

def evenOdd(n):
    if(n % 2 == 0):
        print(n, "even")
    else:
        print(n, "odd")
        
evenOdd(n)