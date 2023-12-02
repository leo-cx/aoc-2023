def part_one(input: str) -> int:
    sum = 0
    for line in input.split("\n"):
        nums = []
        for _, val in enumerate(line):
            if val.isdigit():
                nums.append(int(val))
        if (len(nums) > 0):
            sum += nums[0] * 10 + nums[-1]
    return sum


def part_two(input: str) -> int:
    num_table = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    sum = 0
    for line in input.split("\n"):
        nums = []
        length = len(line)
        for i, _ in enumerate(line):
            if line[i].isdigit():
                nums.append(int(line[i]))
                continue
            for j in range(2, 5):
                if i + j < length and line[i: i + j + 1] in num_table:
                    nums.append(num_table[line[i: i + j + 1]])
                    break
        if (len(nums) > 0):
            sum += nums[0] * 10 + nums[-1]
    return sum


def main():
    with open("input.txt") as calibrations:
        input = calibrations.read().strip()
        print(f"The calibrated sum is {part_one(input)}")
        print(f"The new calibrated sum is {part_two(input)}")


if __name__ == "__main__":
    main()
