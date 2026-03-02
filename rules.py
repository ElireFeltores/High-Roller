import math
from BaseClasses import MultiWorld
from worlds.generic.Rules import set_rule

def roller_score_attainable(world, difficulty):
    for location in world.get_locations():
        set_rule(
            location,
            lambda state, curscore=location.high_roller_score, player=world.player: 
                roller_score_logic_check(
                    slots = min(state.count("Extra Reel", player), 4),
                    coin = state.count("Coin", player),
                    mult = state.count("Score Multiplier", player),
                    double_count = state.count("Double Score Usable", player),
                    difficulty = difficulty,
                    curscore = curscore,
                    items = min(state.count("Jackpot Usable", player) + state.count("Lock On Usable", player) + state.count("Reroll Usable", player), 10)
               ),
        )

slot_scores = [7, 10, 20, 40, 100]
def roller_score_logic_check(slots, coin, mult, double_count, difficulty, curscore, items):
    score = int(slot_scores[slots] * (coin + 3) * (1 + (mult / 10)) + (slot_scores[slots] * (1 + (mult / 10)) * double_count))
    if slots > 0:
        return curscore < int((score / (10 + (10 - items))) * difficulty)
    else:
        return curscore < int((score / 20) * difficulty)

def set_completion_condition(world) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)
