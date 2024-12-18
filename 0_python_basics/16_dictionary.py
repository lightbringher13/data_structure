# dict -> key : value
# ordered, keys are immutable but values are mutable
# no value duplicates last value chosen

# differnt way of dict
# phone_no = dict({
#     "riss": 1234,
#     "jenny": 1234,
#     "jen": 345,
#     "lovo": 456,
#     "riss": 80987  # last value chosen
# })

# phone_no = dict([("riss", 1234), ("jenny", 1234), ("jen", 345), ("lovo", 456)])

phone_no = {
    "riss": 1234,
    "jenny": 1234,
    "jen": 345,
    "lovo": 456,
    "riss": 80987  # last value chosen
}

print(phone_no)

# selcet using key
print(phone_no["jen"])

# selection using get()
print(phone_no.get("riss"))

# change the value
phone_no["riss"] = "34"
print(phone_no)

# can insert any dtypes
phone_no["riss"] = {
    "riss_home": 123,
    "riss_work": 123
}
phone_no["yohan"] = {111, 222, 333}
print(phone_no["yohan"])
print(phone_no)


data = {
    0: "jenny",
    1: "riss",
    2: "leo"
}
# always select using keys
print(data[0])

# deletion
del phone_no["jen"]

# delete return value
print(phone_no.pop("lovo"))

# delete the last added return kay-value pair
print(phone_no.popitem())

# delete whole items
# phone_no.clear()
# print(phone_no)

# access only keys
print(phone_no.keys())

# access only values
print(phone_no.values())

# access all items
print(phone_no.items())

# iterate keys
# iterate according to keys
for i in phone_no:
    print(i)
    print(phone_no[i])

# iterate key-value tuple
for i in phone_no.items():
    print(i)

# copy the dict
print(phone_no)
phone_no2 = phone_no.copy()
print(phone_no2)

# len of dict
print(len(phone_no))

# coding exercise
student_marks = {
    "Jenny": 92,
    "Harry": 78,
    "Dimpy": 56,
    "Rahul": 41,
    "Aniket": 99,
    "Prem": 34
}


def marks_grades(x):
    for i in x:

        if student_marks[i] > 90:
            student_marks[i] = "A+"
        elif student_marks[i] > 80:
            student_marks[i] = "A"
        elif student_marks[i] > 70:
            student_marks[i] = "B+"
        elif student_marks[i] > 60:
            student_marks[i] = "B"
        elif student_marks[i] > 50:
            student_marks[i] = "C"
        elif student_marks[i] > 40:
            student_marks[i] = "D"
        else:
            student_marks[i] = "F"


print(student_marks)
marks_grades(student_marks.keys())
print(student_marks)

# Nested dict and dict & list combination
# Nested dict
student_data = {
    "Ram": {
        "roll_no": 10,
        "age": 20,
        "course": "Python"
    },
    "Moham": {
        "roll_no": 20,
        "age": 22,
        "course": "Java"
    }
}
print(student_data)
print(student_data["Moham"])

# create Mohan's phone_no
print(student_data["Moham"]["roll_no"])
student_data["Moham"]["phone_no"] = 1234
print(student_data["Moham"])

# delete phone_no
# del student_data["Moham"]["phone_no"]

# pop returns poped value
print(student_data["Moham"].pop("phone_no"))
print(student_data["Moham"])

# list within dict
travel_data = {
    "Gujrat": ["Dwarkadhish", "somnath", "statue of unity"],
    "Rajasthan": ["Jaipur", "Udaipur"]
}
print(travel_data["Rajasthan"])

student_data = [
    {"name": "Ram",
     "roll_no": 10,
     "age": 20,
     "course": "Python"
     },
    {"name": "Moham",
     "roll_no": 20,
     "age": 22,
     "course": "Java"
     }
]
print(student_data[1])


def add_new_std(name, roll_no, age, course):
    # first make dictinary
    new_student = {}
    new_student["name"] = name
    new_student["roll_no"] = roll_no
    new_student["age"] = age
    new_student["cousre"] = course
    student_data.append(new_student)


add_new_std("Shyam", 22, 18, "c++")
print(student_data)
