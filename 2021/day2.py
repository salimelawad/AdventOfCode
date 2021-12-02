# advent of code 2021 day 2


def convert_input(text, input):
    return [int(x.split(" ")[1]) for x in input if text in x]


def part1(input):
    forward = convert_input("forward", input)
    up = convert_input("up", input)
    down = convert_input("down", input)
    up = [x * -1 for x in up]
    depth = sum(up + down)
    horizontal = sum(forward)
    return depth * horizontal


def part2(input):
    input = [x.split(" ") for x in input]
    horizontal = 0
    depth = 0
    aim = 0
    for rule, distance in input:
        distance = int(distance)
        if rule == "forward":
            horizontal = horizontal + distance
            depth = depth + aim * distance
        if rule == "up":
            aim = aim - distance
        if rule == "down":
            aim = aim + distance
    return depth * horizontal


def main():
    with open("day2.txt") as f:
        input = f.read().splitlines()
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")


main()
