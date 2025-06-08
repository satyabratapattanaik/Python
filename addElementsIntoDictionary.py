# add ements into dictionary

marks = {}

x = int(input("enter maths : "))
marks.update({"Maths" : x})
y = int(input("enter physics : "))
marks.update({"Physics" : y})
z = int(input("enter chemistry : "))
marks.update({"Chemistry" : z})

print(marks)