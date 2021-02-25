#Author: ALJ (AMDG) 2/25/21

def build_vehicle(input1, input2, input3, input4):
    wheels = input1
    axels = input2
    doors = input3
    color = input4
    return("The car has {0} wheels, {1} doors, {2} axels, and is the color {3}.".format(wheels, doors, axels, color))

ask1 = input("How many wheels? ")
ask2 = input("How many axels? ")
ask3 = input("How many doors? ")
ask4 = input("What color? ")

print(build_vehicle(ask1, ask2, ask3, ask4))