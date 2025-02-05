#A python program that checks for room temperature

temperature = 23
if temperature > 25 :
    print("It is too hot")
else :
    print("It is too cold")

#A program that returns the largest number
first = 89
second = 30
third = 56

if first > second and first > third :
    print(first,"is the largest number")
elif second > first and second > third:
    print(second,"is the smallest number")
else:
    print(third,"is the largest number")

#Program to check a number and return whether the number is even or odd
num = 7
number = 14

if (num or number) == 0 :
    print(number or num,"is zero")

if (num % 2) == 0 :
    print(num,"is even")
else :
    print(num,"is odd")

if (number % 2) != 0 :
    print(number,"is odd")
else :
    print(number,"is even")

if (num,number) == 0 :
    print(number,num,"is zero")
