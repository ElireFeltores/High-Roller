from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Item, ItemClassification
from ..oot.Options import world_options

if TYPE_CHECKING:
    from .world import HighRollerWorld

item_ids = {
        "Extra Reel": 1,
        "Jackpot Usable": 2,
        "Double Score Usable": 3,
        "Lock On Usable": 4,
        "Reroll Usable": 5,
        "Score Multiplier": 6,
        "Coin": 7,
        "Let's Go Gambling!": 8,
        "Unlucky Thirteens": 9,
        "EAV's Regards": 10,
    }

default_item_classifications = {
    "Extra Reel": ItemClassification.progression,
    "Jackpot Usable": ItemClassification.progression,
    "Double Score Usable": ItemClassification.progression,
    "Lock On Usable": ItemClassification.progression,
    "Reroll Usable": ItemClassification.progression,
    "Score Multiplier": ItemClassification.progression,
    "Coin": ItemClassification.progression,
    "Let's Go Gambling!": ItemClassification.filler,
    "Unlucky Thirteens": ItemClassification.filler,
    "EAV's Regards": ItemClassification.filler,
}

class HighRollerItem(Item):
    game = "High Roller"

def get_random_filler_item_name(world: HighRollerWorld) -> str:
    rand = world.random.randint(0, 51)
    if rand < 25:
        return "Let's Go Gambling!"
    if rand < 50:
        return "Unlucky Thirteens"
    return "EAV's Regards"

def create_all_items(world: HighRollerWorld) -> None:
    itempool: list[Item] = [
        world.create_item("Extra Reel"),
        world.create_item("Extra Reel"),
        world.create_item("Extra Reel"),
        world.create_item("Extra Reel"),
        world.create_item("Jackpot Usable"),
        world.create_item("Jackpot Usable"),
        world.create_item("Jackpot Usable"),
        world.create_item("Double Score Usable"),
        world.create_item("Double Score Usable"),
        world.create_item("Double Score Usable"),
        world.create_item("Lock On Usable"),
        world.create_item("Lock On Usable"),
        world.create_item("Reroll Usable"),
        world.create_item("Reroll Usable"),
        world.create_item("Score Multiplier"),
        world.create_item("Score Multiplier"),
        world.create_item("Score Multiplier"),
        world.create_item("Score Multiplier"),
        world.create_item("Score Multiplier"),
        world.create_item("Score Multiplier"),
        world.create_item("Score Multiplier"),
        world.create_item("Score Multiplier"),
        world.create_item("Score Multiplier"),
        world.create_item("Score Multiplier"),
        world.create_item("Coin"),
        world.create_item("Coin"),
        world.create_item("Coin"),
        world.create_item("Coin"),
        world.create_item("Coin"),
        world.create_item("Coin"),
        world.create_item("Coin"),
        world.create_item("Coin"),
        world.create_item("Coin"),
        world.create_item("Coin"),
    ]
    if world.options.crit_items > 1:
        itempool.append(world.create_item("Coin")),
        itempool.append(world.create_item("Coin")),
        itempool.append(world.create_item("Coin")),
    if world.options.crit_items > 2:
        itempool.append(world.create_item("Coin")),
        itempool.append(world.create_item("Coin")),
        itempool.append(world.create_item("Coin")),
        itempool.append(world.create_item("Score Multiplier")),
        itempool.append(world.create_item("Score Multiplier")),
        itempool.append(world.create_item("Score Multiplier")),
    if world.options.crit_items > 3:
        itempool.append(world.create_item("Coin")),
        itempool.append(world.create_item("Coin")),
        itempool.append(world.create_item("Score Multiplier")),
        itempool.append(world.create_item("Score Multiplier")),
        itempool.append(world.create_item("Jackpot Usable")),
        itempool.append(world.create_item("Double Score Usable")),
        itempool.append(world.create_item("Lock On Usable")),
        itempool.append(world.create_item("Reroll Usable")),
    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    world.multiworld.itempool += itempool
