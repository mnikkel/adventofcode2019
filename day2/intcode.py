CODE = [
    1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 1, 13, 19, 2, 9, 19, 23,
    1, 23, 6, 27, 1, 13, 27, 31, 1, 31, 10, 35, 1, 9, 35, 39, 1, 39, 9, 43, 2,
    6, 43, 47, 1, 47, 5, 51, 2, 10, 51, 55, 1, 6, 55, 59, 2, 13, 59, 63, 2, 13,
    63, 67, 1, 6, 67, 71, 1, 71, 5, 75, 2, 75, 6, 79, 1, 5, 79, 83, 1, 83, 6,
    87, 2, 10, 87, 91, 1, 9, 91, 95, 1, 6, 95, 99, 1, 99, 6, 103, 2, 103, 9,
    107, 2, 107, 10, 111, 1, 5, 111, 115, 1, 115, 6, 119, 2, 6, 119, 123, 1,
    10, 123, 127, 1, 127, 5, 131, 1, 131, 2, 135, 1, 135, 5, 0, 99, 2, 0, 14, 0
]


def run_code(exe):
    i = 0
    while i < len(exe):
        op = exe[i]
        if op == 1:
            a, b, c = exe[i + 1], exe[i + 2], exe[i + 3]
            exe[c] = exe[a] + exe[b]
            i += 4
        elif op == 2:
            a, b, c = exe[i + 1], exe[i + 2], exe[i + 3]
            exe[c] = exe[a] * exe[b]
            i += 4
        elif op == 99:
            return exe[0]


def part1(code):
    code[1] = 12
    code[2] = 2
    return run_code(code)


def part2(code):
    for noun in range(99):
        for verb in range(99):
            code[1] = noun
            code[2] = verb
            if run_code(code.copy()) == 19690720:
                return 100 * noun + verb


print(part1(CODE.copy()))
print(part2(CODE.copy()))
