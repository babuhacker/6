# Program to Find the Factors of a Number

num = int(input("enter a number here:"))

for i in range(1, num+1):
    if num % i == 0:
        print(i)
