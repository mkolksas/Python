#Built-in functions/Standard-library functions

y = max(45, 89, 75, 69, 56, 43)
print("The maximum value is",y)

x = min(23, 45, 67 ,89 ,34)
print("The minimum value is",x)

#User-defined functions
def school():
    print("eMobilis")

school()

def add():
    num1 = 5
    num2 = 3
    print(num1 + num2)

add()

#Parameter/Variable and Argument/Value
def multiply(a , b):
    print(a * b)

multiply(5, 4)
multiply(24, 20)

def employee  (name, age, gender, salary, position):
    print(name,age,gender,salary,position)

employee("Maureen",25,"Female",560000,"CEO")
employee("John",32,"male",160000,"Managing Director")
employee("Max",21,"male",90000,"Intern")
employee("Judy",27,"Female",200000,"Manager")
employee("Emma",41,"Female",350000,"Accountant")

#A program to display details of five patients.Using a user-defined function, implement parameter and argument
#fullname, age, gender, disease
def patients(names, age, gender, disease):
    print(names, age, gender, disease)

patients("John Fadi", 56, "Male","Pneumonia")
patients("Tamara Dilty", 17, "Female","Broken leg")
patients("Jezz Chan", 22, "Male","Concussion")
patients("Elsie Bonio", 28, "Female","Dislocated Shoulder")
patients("Lulu Gini", 42, "Male","Burns")

