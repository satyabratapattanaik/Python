food = input("Food : ")
eat = "Yes" if food == "Cake" else "No"
print(eat)

print("Sweet") if food == "Cake" or food == "Jalebi" else print("not sweet")

age = int(input("age : "))
vote = ("Yes", "No") [age<18]
print(vote)
