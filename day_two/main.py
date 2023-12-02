def part_one(input: str) -> int:
    sum = 0
    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    for line in input.split("\n"):
        # ["Game 1", "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"]
        game = line.split(": ")
        id = int(game[0][5:])
        # ["3 blue, 4 red", "1 red, 2 green, 6 blue", "2 green"]
        rounds = game[1].split("; ")
        valid = True
        # "3 blue", "4 red"
        for values in rounds:
            colors = {
                "red": 0,
                "green": 0,
                "blue": 0
            }
            # "3", "blue"
            quantities = values.split(", ")
            for pair in quantities:
                num, color = pair.split(" ")
                colors[color] += int(num)
            if colors["red"] > 12 or colors["green"] > 13 or colors["blue"] > 14:
                valid = False
        if valid:
            sum += id
    return sum

def part_two(input: str) -> int:
    pset = 0
    # "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    for line in input.split("\n"):
        # ["Game 1", "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"]
        game = line.split(": ")
        # ["3 blue, 4 red", "1 red, 2 green, 6 blue", "2 green"]
        rounds = game[1].split("; ")
        max = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        # "3 blue", "4 red"
        for values in rounds:
            colors = {
                "red": 0,
                "green": 0,
                "blue": 0
            }
            # "3", "blue"
            quantities = values.split(", ")
            for pair in quantities:
                num, color = pair.split(" ")
                colors[color] += int(num)
                if colors[color] > max[color]:
                    max[color] = colors[color]
        pset += (max["red"] * max["green"] * max["blue"])
    return pset


def main():
    with open("input.txt") as games:
        input = games.read().strip()
        print(f"The sum of the playable games is {part_one(input)}.")
        print(f"The sum of the power sets is {part_two(input)}.")


if __name__ == "__main__":
    main()
