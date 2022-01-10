import sys
from os import path

import pandas as pd
from more_itertools import chunked

file_path = path.dirname(path.realpath(__file__)) + "/input.txt"
data = open(file_path, mode='r')
text = [x.rstrip("\n") for x in data.readlines()]

all_x_values = []
all_y_values = []


def generate_coordinates(input):
    coordinate_sets = input.split(" -> ")
    z = [x.split(",") for x in coordinate_sets]
    z = [list(map(int, x)) for x in z]
    for x in z:
        all_x_values.append(x[0])
        all_y_values.append(x[1])
    return z


coordinates = list(map(generate_coordinates, text))
max_width = max(all_x_values)
max_height = max(all_y_values)

map_df = pd.DataFrame(index=range(max_height + 1), columns=range(max_width + 1))
map_df.fillna(0, inplace=True)
for coordinate in coordinates:
    if coordinate[0][0] == coordinate[1][0] or coordinate[0][1] == coordinate[
            1][1]:
        for x in range(coordinate[0][0], coordinate[1][0] + 1):
            for y in range(coordinate[0][1], coordinate[1][1] + 1):
                map_df.at[y, x] += 1
        pass
pass

total_intersections = list(
    filter(lambda x: x >= 2,
           map_df.values.flatten().tolist()))
print(len(total_intersections))