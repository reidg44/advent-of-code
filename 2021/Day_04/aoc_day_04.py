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

all_dfs = dict()
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


for bingo_card, chunk in enumerate(chunked_lines):
    integers = [x.split(" ") for x in chunk]
    integers = [remove_empty_vals(x) for x in integers]
    all_dfs[str(bingo_card)] = pd.DataFrame(integers)


def check_for_bingo(bingo_number):
    cards_to_delete = []
    for bingo_card, df in all_dfs.items():
        is_bingo = False
        if df.values.flatten().tolist().count("X") >= 5:
            for col in df.columns:
                if not is_bingo:
                    is_bingo = df[col].values.tolist() == bingo
            for index, data in df.iterrows():
                if not is_bingo:
                    is_bingo = data.values.tolist() == bingo
            if is_bingo:
                got_bingo(bingo_card, df, bingo_number)
                cards_to_delete.append(bingo_card)
                pass
    for card in cards_to_delete:
        all_dfs.pop(card)


def got_bingo(bingo_card, df, bingo_number):
    print(f"BINGO! Card: {bingo_card}")
    all_values = df.values.flatten().tolist()
    only_ints = sum(list(filter(lambda x: type(x) == int, all_values)))
    # all_dfs.pop(bingo_card)
    if len(all_dfs.items()) == 1:
        for bingo_card, df in all_dfs.items():
            all_values = df.values.flatten().tolist()
            only_ints = sum(list(filter(lambda x: type(x) == int, all_values)))
            print(f'Answer #2: {only_ints * bingo_number}')
        sys.exit()


for bingo_number in bingo_numbers:
    new_dfs = dict()
    for bingo_card, df in all_dfs.items():
        new_df = df.replace(bingo_number, "X")
        new_dfs[bingo_card] = new_df
    all_dfs = new_dfs
    check_for_bingo(bingo_number)

pass
