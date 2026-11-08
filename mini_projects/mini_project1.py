name = input("Enter name : ")
age = float(input("Enter age: "))

if age > 18:
    print(f"{name} is eligible for jobs")
else:
    print(f"{name} is not eligible for jobs")