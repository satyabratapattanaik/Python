# WAP to find the sum of n natural numbers

n = int(input("Enter a number : "))

sum = 0
for i in range(1, n+1):
    sum += i

print("Total sum =", sum)