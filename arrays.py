courses = ["MIT","Cybersecurity","Datascience"]
print(courses)

#Accessing an element, starts counting at 0
print(courses[2])

#Looping through an array
for x in courses:
    print("Course is",x)

#Adding a new element into an array
courses.append("Laravel")
print(courses)

#Removung an element from an array
courses.remove("Cybersecurity")
print(courses)