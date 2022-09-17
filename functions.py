def mean(value):
    # if type(value) == dict:
    if isinstance(value, dict):
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)

    return the_mean


print(mean([1, 4, 5]))


def convert(amount):
    output = amount * 1.75
    return output


print(convert(10))


student_grades = [9.1, 8.8, 7.5]
print(mean(student_grades))
student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
print(mean(student_grades))
