#Write a program that checks whether a number is a prime number is or not

try:
    num=int(input("Enter a number: "))
    if num <= 1:
        print(num,"is not a prime number")
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                print(num,"is not a prime number")
                break
        else:
            print(num,"is a prime number")

except ValueError:
    print("Invalid input")
