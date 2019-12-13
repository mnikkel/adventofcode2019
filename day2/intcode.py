code = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,2,9,19,23,1,23,6,27,1,13,27,31,1,31,10,35,1,9,35,39,1,39,9,43,2,6,43,47,1,47,5,51,2,10,51,55,1,6,55,59,2,13,59,63,2,13,63,67,1,6,67,71,1,71,5,75,2,75,6,79,1,5,79,83,1,83,6,87,2,10,87,91,1,9,91,95,1,6,95,99,1,99,6,103,2,103,9,107,2,107,10,111,1,5,111,115,1,115,6,119,2,6,119,123,1,10,123,127,1,127,5,131,1,131,2,135,1,135,5,0,99,2,0,14,0]

part1 = code.copy()
part1[1] = 12
part1[2] = 2

for pos, op in enumerate(part1[::4]):
    p = pos * 4
    if op == 1:
        a, b, c = part1[p+1], part1[p+2], part1[p+3]
        part1[c] = part1[a] + part1[b]
    elif op == 2:
        a, b, c = part1[p+1], part1[p+2], part1[p+3]
        part1[c] = part1[a] * part1[b]
    elif op == 99:
        print(part1[0])

for noun in range(99):
    for verb in range(99):
        part2 = code.copy()
        part2[1] = noun
        part2[2] = verb
        for pos, op in enumerate(part2[::4]):
            p = pos * 4
            if op == 1:
                a, b, c = part2[p+1], part2[p+2], part2[p+3]
                part2[c] = part2[a] + part2[b]
            elif op == 2:
                a, b, c = part2[p+1], part2[p+2], part2[p+3]
                part2[c] = part2[a] * part2[b]
            elif op == 99:
                if part2[0] == 19690720:
                    print(100*noun+verb)
                    break
