#Author: ALJ (AMDG) 2/25/21

def build_vehicle():
    wheels = 4
    doors = 4
    axels = 2
    color = 'red'
    return("The car has {0} wheels, {1} doors, {2} axels, and is the color {3}.".format(wheels, doors, axels, color))

print(build_vehicle())
print(build_vehicle())
print(build_vehicle())