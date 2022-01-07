import sys
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
removed_cards = []
removed_card_numbers = []

bingo = [
    "X",
    "X",
    "X",
    "X",
    "X",
]


def remove_empty_vals(x):
    return [int(i) for i in x if i != ""]


for chunk in chunked_lines:
    integers = [x.split(" ") for x in chunk]
    integers = [remove_empty_vals(x) for x in integers]
    all_dfs.append(pd.DataFrame(integers))


def check_for_bingo(bingo_number):

    for bingo_card, df in enumerate(all_dfs):
        is_bingo = False
        if df.values.flatten().tolist().count("X") >= 5:
            for col in df.columns:
                is_bingo = df[col].values.tolist() == bingo
            for index, data in df.iterrows():
                is_bingo = data.values.tolist() == bingo
            if is_bingo:
                got_bingo(bingo_card, df, bingo_number)
                pass


def got_bingo(bingo_card, df, bingo_number):
    print(f"BINGO! Card: {bingo_card}")
    all_values = df.values.flatten().tolist()
    only_ints = sum(list(filter(lambda x: type(x) == int, all_values)))
    if bingo_card not in removed_card_numbers:
        removed_card_numbers.append(bingo_card)
        removed_cards.append(df)
    if len(removed_cards) == (len(all_dfs) - 1):
        last_card = list(
            set(range(len(all_dfs))).difference(set(removed_card_numbers)))[0]
        all_values = all_dfs[last_card].values.flatten().tolist()
        only_ints = sum(list(filter(lambda x: type(x) == int, all_values)))
        print(f'Answer #2: {only_ints * bingo_number}')
        sys.exit()


for bingo_number in bingo_numbers:
    new_dfs = []
    for df in all_dfs:
        new_df = df.replace(bingo_number, "X")
        new_dfs.append(new_df)
    all_dfs = new_dfs
    check_for_bingo(bingo_number)

pass
