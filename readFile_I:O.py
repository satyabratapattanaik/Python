# Reading a file

# line = f.readline()

f = open("demo.txt", "r")
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
f.close()

# data = f.read()

f= open("demo.txt", "r")
data = f.read()
print(data)
f.close()

# data = f.read()
# line = f.readline()

f = open("demo.txt", "r")
data = f.read()
print(data)
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
f.close()

