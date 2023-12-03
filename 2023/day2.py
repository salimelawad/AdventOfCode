# read txt file as a list of strings
import re

with open("2023/data/day2.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

# build game parser
games = {}
for line in data:
    line = line[5::]
    game_num_list = line.split(":")
    game_number = game_num_list[0]
    subgames = game_num_list[1].split(";")
    cur_game = {}
    for i, single_game in enumerate(subgames):
        subgame = {}
        blue = re.search(r"(\d*) blue", single_game)
        green = re.search(r"(\d*) green", single_game)
        red = re.search(r"(\d*) red", single_game)
        if blue:
            subgame["blue"] = int(blue.group(1))
        if green:
            subgame["green"] = int(green.group(1))
        if red:
            subgame["red"] = int(red.group(1))

        cur_game[i] = subgame
    games[game_number] = cur_game

# PART 1
# find valid games with a max of 12 red, 13 green, and 14 blue:

valid_games = []
for game in games:
    valid = True
    for subgame in games[game]:
        if valid == False:
            break
        if (
            "red" in games[game][subgame]
            and games[game][subgame]["red"] > 12
            or "green" in games[game][subgame]
            and games[game][subgame]["green"] > 13
            or "blue" in games[game][subgame]
            and games[game][subgame]["blue"] > 14
        ):
            valid=False
    if valid:
        valid_games.append(game)

print(sum([int(game) for game in valid_games]))

# PART 2
## find the min set of cubes for each game
min_game_power = []
for game in games:
    min_set = {"blue": 0, "green": 0, "red": 0}
    for subgame in games[game]:
        if "red" in games[game][subgame] and games[game][subgame]["red"] > min_set["red"]:
            min_set["red"] = games[game][subgame]["red"]
        if "green" in games[game][subgame] and games[game][subgame]["green"] > min_set["green"]:
            min_set["green"] = games[game][subgame]["green"]
        if "blue" in games[game][subgame] and games[game][subgame]["blue"] > min_set["blue"]:
            min_set["blue"] = games[game][subgame]["blue"]
    min_game_power.append(min_set["red"] * min_set["green"] * min_set["blue"])

print(sum(min_game_power))