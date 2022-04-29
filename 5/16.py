"""Write a program to check whether a given number is prime or not
Program should accept an input from the user and display whether the number is prime or not
"""
num=int(input("enter a number"))
flag=False
for i in range(2,num):
    if (num%i)==0:
        flag=True
        break
if flag:
    print("entered number is not a prime number")
else:
    print("enter number is a prime number")
