monday_temperatures = [9.1, 8.8, 7.6]

for temp in monday_temperatures:
    print(round(temp))

for letter in "hello":
    print(letter.title())


student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
# for grades in student_grades.items():
# for grades in student_grades.keys():
for grades in student_grades.values():
    print(grades)

phone_numbers = {"John": "+37682929928", "Marry": "+42399820919"}

for key, value in phone_numbers.items():
    print(
        f"{key} has as phone number {value[:2]} ({value[2:5]}) {value[5:8]}-{value[8:]}"
    )


a = 3

while a > 0:
    print(a)
    a -= 1

username = ""

# while username != "pypy":
#     username = input("Enter username: ")

while True:
    username = input("Enter username: ")
    if username == "pypy":
        break
    else:
        continue


