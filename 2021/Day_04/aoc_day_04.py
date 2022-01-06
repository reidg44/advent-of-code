from os import path
import pandas as pd
from more_itertools import chunked

file_path = path.dirname(path.realpath(__file__)) + "/input.txt"
data = open(file_path, mode='r')
inputs = [x.rstrip("\n") for x in data.readlines()]
removed_lines = list(filter(lambda x: x != "", inputs))
bingo_numbers = [int(x) for x in removed_lines[0].split(",")]
removed_lines.pop(0)
chunked_lines = list(chunked(removed_lines, 5))
all_dfs = []

for chunk in chunked_lines:
    integers = [x.split(" ") for x in chunk]
    # remove empty strings from list
    integers = list(lambda x: x != "", integers)
    pass
pass