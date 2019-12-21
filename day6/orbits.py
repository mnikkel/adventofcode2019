f = open('input')
INPUT = list(map(str.rstrip, list(f)))


def generate_orbits(input):
    orbits = {}
    for orbit in INPUT:
        a, b, c = orbit.partition(')')
        if a in orbits:
            orbits[a].append(c)
        else:
            orbits[a] = [c]
    return orbits


def count_orbits(orbits, origin, weight):
    if origin in orbits:
        count = (len(orbits[origin]) * weight)
        indirect = 0
        for body in orbits[origin]:
            indirect += count_orbits(orbits, body, weight + 1)
        return count + indirect
    else:
        return 0


def part1():
    orbits = generate_orbits(INPUT)
    print(count_orbits(orbits, 'COM', 1))


part1()
