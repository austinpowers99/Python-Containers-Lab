# Here’s the basic syntax of a list comprehension:
# [<expression> for <item> in <list>]
# This reads as: I want <expression> for each <item> in <list>

# Exercise 1
students = ["Janica", "Gurman", "Cesar", "Sam"]

print("Second student's name:", students[1])
print("Last student's name:", students[-1])

# Exercise 2
foods = ("oreos", "cheesecake", "pie", "tart")
for i in range(len(foods)):
    print(f"{foods[i]} is a good food.")

# Exercise 3
for i in range(len(foods) - 2, len(foods)):
    print (f"{foods[i]} is a good food.")


# Exercise 4
home_town = {
    "city": "San Francisco",
    "state": "California",
    "population": 715717
}
print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")


# Exercise 5
for key, value in home_town.items():
    print(f"{key} = {value}")


# Exercise 6
cohort = []

for index, student in enumerate(students):
    fav_food = foods[index]
    student_dict = {
        'student': student,
        "fav_food": fav_food
    }
    cohort.append(student_dict)

for item in cohort:
    print(item)

# Exercise 7
awesome_students = [f"{name} is wesome!" for name in students]
for student in awesome_students:
    print(student)


# Exercise 8
for food in [food for food in foods if "a" in food]:
    print(food)