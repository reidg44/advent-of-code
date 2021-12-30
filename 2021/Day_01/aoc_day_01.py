from os import path

script_dir = path.dirname(path.realpath(__file__)) + "/"
file_path = script_dir + "input.txt"

data = open(file_path, mode='r')
inputs = [int(x.rstrip("\n")) for x in data.readlines()]

num_higher_than_before = list(
    filter(lambda x: x[1] > inputs[x[0] - 1], enumerate(inputs)))
print(len(num_higher_than_before))

sum_of_threes = [
    sum([x[1], inputs[x[0] + 1], inputs[x[0] + 2]])
    for x in list(enumerate(inputs))[:-2]
]
sum_higher_than_before = list(
    filter(lambda x: x[1] > sum_of_threes[x[0] - 1], enumerate(sum_of_threes)))
print(len(sum_higher_than_before))
data.close()