from __future__ import annotations
import typing
from BaseClasses import Location
class LocData(typing.NamedTuple):
    id: int
    region: str
    score: int

# Yes a lot of this location code was taken from Yacht Dice's APWorld
class HighRollerLocation(Location):
    game = "High Roller"
    def __init__(self, player: int, name: str, score: int, address: typing.Optional[int], parent):
        super().__init__(player, name, address, parent)
        self.high_roller_score = score
all_locations = {}
starting_index = 16871244500
def all_locations_fun(max_score):
    return {f"{i} Score": LocData(starting_index + i, "Hold", i) for i in range(1, max_score + 1)}
def ini_locations(goal_score, max_score, check_density):
    scores = []
    highest_score = 0
    start_score = 0
    i = 0
    current_score = 0
    while current_score < max_score:
        i = i + 1
        percentage = i**1.588 / (i**0.22 * check_density)
        current_score = int(start_score + 1 + percentage)
        if current_score <= highest_score:
            current_score = highest_score + 1
        highest_score = current_score
        if highest_score > max_score:
            break
        scores += [current_score]
    if goal_score != max_score:
        if goal_score not in scores:
            closest_num = min(scores, key=lambda x: abs(x - goal_score))
            scores[scores.index(closest_num)] = goal_score
    scores += [max_score]
    location_table = {f"{score} Score": LocData(starting_index + score, "Hold", score) for score in scores}
    return location_table

all_locations = all_locations_fun(2000)