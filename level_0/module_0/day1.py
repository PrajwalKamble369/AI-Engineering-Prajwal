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

# homework
# q1
num = float(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

# q2
num = float(input("Enter a number: "))
print(num ** 2)

# q3
for i in range(1,21):
    print(i)

counter = 1
while counter <= 20:
    print(counter)
    counter += 1

# q4
def add(a,b):
    sums = a +b
    return sums