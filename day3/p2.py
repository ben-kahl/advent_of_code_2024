import re

pattern = re.compile(r"mul\(\d*,\d*\)")
param = re.compile(r"\d+")
do_pattern = re.compile(r"do\(\)")
dont_pattern = re.compile(r"don\'t\(\)")


def parse_instruction(ins):
    m1, m2 = param.findall(ins)
    return int(m1) * int(m2)


def perform_muls(instructions):
    sum = 0
    for ins in instructions:
        sum += parse_instruction(ins)
    return sum


with open("input.txt", 'r') as file:
    text = file.read()

instructions = pattern.findall(text)
print(perform_muls(instructions))
