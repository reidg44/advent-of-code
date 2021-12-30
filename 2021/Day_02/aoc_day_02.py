from os import path

file_path = path.dirname(path.realpath(__file__)) + "/input.txt"

data = open(file_path, mode='r')
inputs = [x.rstrip("\n") for x in data.readlines()]

vertical_position = 0
horizontal_position = 0
aim = 0

for x in inputs:
    value = int(x.split(" ")[1])
    if x.startswith("forward"):
        horizontal_position += value
        vertical_position += (value * aim)
    elif x.startswith("up"):
        # vertical_position -= value
        aim = aim + value
    elif x.startswith("down"):
        # vertical_position += value
        aim = aim - value
    pass

print(f"Vertical position: {vertical_position}")
print(f"Horizontal position: {horizontal_position}")

print(vertical_position * horizontal_position)
pass