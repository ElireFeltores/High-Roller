from collections.abc import Mapping
from typing import Any
from worlds.AutoWorld import World
from worlds.generic.Rules import set_rule
from . import items, locations, options, rules, web_world
from .locations import HighRollerLocation
from BaseClasses import Region, Entrance, Item, ItemClassification

class HighRollerWorld(World):
    """
    High Roller is a slot machine styled game, where you collect various buffs to increase your scores on the slots.
    """
    game = "High Roller"
    web = web_world.HighRollerWebWorld()
    options_dataclass = options.HighRollerOptions
    options: options.HighRollerOptions
    location_name_to_id = {name: data.id for name, data in locations.all_locations.items()}
    item_name_to_id = items.item_ids
    origin_region_name = "Main"
#    def set_rules(self):
#        for location in self.multiworld.get_locations(self.player):
#            set_rule(
#                location,
#                lambda state, curscore=location.score, player=self.player:
#                    state.count("Apple", player) * 5 + state.count("Banana", player) * 50
#                    >= curscore,
#            )
    def create_regions(self) -> None:
        location_table = locations.ini_locations(self.options.goal_score, self.options.max_score, self.options.check_density)
        main = Region("Main", self.player, self.multiworld)
        hold = Region("Hold", self.player, self.multiworld)
        hold.locations = [
            HighRollerLocation(self.player, loc_name, loc_data.score, loc_data.id, hold)
            for loc_name, loc_data in location_table.items()
            if loc_data.region == hold.name
        ]
        print(hold.locations)
        victory_location_name = f"{self.options.goal_score} Score"
        self.get_location(victory_location_name).address = None
        self.get_location(victory_location_name).place_locked_item(
            Item("Victory", ItemClassification.progression, None, self.player)
        )
        connection = Entrance(self.player, "New Hold", main)
        main.exits.append(connection)
        connection.connect(hold)
        self.multiworld.regions += [main, hold]
    def set_rules(self) -> None:
        rules.roller_score_attainable(self, self.options.difficulty)
        rules.set_completion_condition(self)
    def fill_slot_data(self) -> dict[str, Any]:
        return self.options.as_dict("goal_score")
    def create_items(self) -> None:
        items.create_all_items(self)
    def create_item(self, name: str) -> items.HighRollerItem:
        return items.HighRollerItem(name, items.default_item_classifications[name], items.item_ids[name], self.player)
    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)
    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict(
            "difficulty", "max_score", "goal_score", "check_density", "death_link"
        )
