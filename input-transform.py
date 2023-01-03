import json

with open("input.txt", "r") as my_file:
    input_raw = my_file.readlines()

for pos, inp in enumerate(input_raw):
    input_raw[pos] = inp.rstrip()

input = []
for inp in input_raw:
    num_1 = int(inp[: inp.find("-")])
    num_2 = int(inp[inp.find("-") + 1 : inp.find(" ")])
    char = inp[inp.find(" ") + 1 : inp.find(":")]
    password = inp[inp.find(": ") + 2 :]
    input.append((num_1, num_2, char, password))

with open("input.json", "w") as my_file:
    json.dump(input, my_file)
