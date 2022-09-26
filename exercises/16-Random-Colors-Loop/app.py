import random

def get_color(color_number=4):
    # making sure is a number and not a string
    color_number = int(color_number)

    switcher={
                  0:'red',
                  1:'yellow',
                  2:'blue',
                  3:'green',
                  4:'black'
              }
    return switcher.get(color_number,"Invalid Color Number")


def get_allStudentColors():
    students_array = []
    for x in range(10):
        randomNum = random.randint(0, 3)
        newColor = get_color(randomNum)
        students_array.append(newColor)
    return students_array


print(get_allStudentColors())