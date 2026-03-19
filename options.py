from dataclasses import dataclass
from typing import TYPE_CHECKING
from Options import Toggle, Choice, PerGameCommonOptions, Range, NamedRange, DeathLink
import datetime
if TYPE_CHECKING:
    from .world import HighRollerWorld

class Difficulty(Choice):
    """The logic difficulty for the slot. Higher difficulty = higher scores expected with less items."""
    display_name = "Logic Difficulty"
    option_easy = 5
    option_medium = 6
    option_hard = 7
    option_expert = 8
    option_mania = 9
    default = 6
class ScoreForLastCheck(NamedRange):
    """The score of the last check in the slot."""
    display_name = "Final Check Score"
    range_start = 500
    range_end = 2000
    default = 700
    special_range_names = {
        "small": 700,
        "medium": 1000,
        "large": 1400,
        "extreme": 2000,
    }
#    if datetime.datetime.today().month == 4 and datetime.datetime.today().day == 1:
#        special_range_names["fragmented"] = -1
class ScoreForGoal(NamedRange):
    """The score needed to goal the slot."""
    display_name = "Goal Score"
    range_start = 500
    range_end = 2000
    default = 600
    special_range_names = {
        "light": 600,
        "medium": 800,
        "heavy": 1200,
        "extreme": 2000,
    }
class CheckDensity(Range):
    """The density of locations in the slot."""
    display_name = "Check Density"
    range_start = 1
    range_end = 15
    default = 3
class AllIn(Toggle):
    """Creates one location for every score count, up to 2,000.
    Warning: This setting will override Check Density and Max Score."""
    display_name = "All In"
class ImportantItems(Choice):
    """The quantity of important items in the slot."""
    display_name = "Important Items"
    option_minimal = 1
    option_sparse = 2
    option_filled = 3
    option_overloaded = 4
    default = 2
class AddUseful(Toggle):
    """Adds useful 'X points' items to the pool, which are points you start each run with."""
    display_name = "Add Points"
class HRDeathLink(DeathLink):
    __doc__ = DeathLink.__doc__ + "\n\nGetting too many scythes in a line (i.e. getting negative score) sends a deathlink.\nReceiving a deathlink will cause a loss of 1-3 coins, depending on max coin count."

@dataclass
class HighRollerOptions(PerGameCommonOptions):
    difficulty: Difficulty
    max_score: ScoreForLastCheck
    goal_score: ScoreForGoal
    check_density: CheckDensity
    all_in: AllIn
    crit_items: ImportantItems
    death_link: HRDeathLink
    add_points: AddUseful
