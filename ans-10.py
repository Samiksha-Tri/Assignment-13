""" Write a Python script to create a list, where each element of the list is a digit of a
given number"""

n=int(input("enter a number :"))
l1=[]
while n>0:
    rem=n%10
    l1.insert(0,rem)
    n=n//10
print(l1)    