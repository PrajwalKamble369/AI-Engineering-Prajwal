# Python Foundation
# Concept 1 : Variable
# A variable stores the data.
name = "Xavier"    # string
age = 28           # interger
salary = 25000.10  # float
is_student = True  # boolean

# print values
print(name)
print(age)
print(salary)

# check type
print(type(name))
print(type(age))

# input from user
name = input("Enter your name: ")
print("Welcome", name)

# operators
# arithmetic
a = 10
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)

# conditional
age > 20
if age > 18:
    print("Adult")
else:
    print("Minor")

# loops
# for
for i in range(5):
    print(i)

#while
count = 1
while count <= 5:
    print(count)
    count +=1

# functions
def greet(name):
    print("Hello", name)

print(greet("Xavier"))