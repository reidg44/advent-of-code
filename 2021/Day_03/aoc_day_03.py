from os import path
import pandas as pd
from math import floor

file_path = path.dirname(path.realpath(__file__)) + "/input.txt"
data = open(file_path, mode='r')
inputs = [list(x.rstrip("\n")) for x in data.readlines()]
threshold = floor(len(inputs) / 2)

df = pd.DataFrame(inputs)
epsilon_rate = ""
gamma_rate = ""
for column in df.columns:
    df[column] = df[column].astype(int)
    col_val = 1 if sum(df[column]) > threshold else 0
    epsilon_rate += str(col_val)
    gamma_rate += str(0 if col_val == 1 else 1)
power_rate = int(epsilon_rate, 2) * int(gamma_rate, 2)
print("Part 1: ", power_rate)
pass

for column in df.columns:
    threshold = len(df.index) / 2
    col_val = 1 if sum(df[column]) >= threshold else 0
    # drop rows where column value is not equal to col_val
    df = df[df[column] == col_val]
    if len(df.index) == 1:
        break
o2_remaining_row = df.values.tolist()[0]
o2_remaining_row_str = [str(x) for x in o2_remaining_row]
oxygen_generator_rating = int("".join(o2_remaining_row_str), 2)
print("Oxygen Generator Rating: ", oxygen_generator_rating)

# reset dataframe
co2_df = pd.DataFrame(inputs)
for column in co2_df.columns:
    co2_df[column] = co2_df[column].astype(int)
    threshold = len(co2_df.index) / 2
    col_sum = sum(co2_df[column])
    col_val = 0 if col_sum >= threshold else 1
    # drop rows where column value is not equal to col_val
    co2_df = co2_df[co2_df[column] == col_val]
    if len(co2_df.index) == 1:
        break
co2_remaining_row = co2_df.values.tolist()[0]
co2_remaining_row_str = [str(x) for x in co2_remaining_row]
co2_scrubber_rating = int("".join(co2_remaining_row_str), 2)
print("Co2 Scrubber Rating: ", co2_scrubber_rating)

print("Part 2: ", oxygen_generator_rating * co2_scrubber_rating)