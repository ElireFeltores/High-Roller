from dataclasses import dataclass
from typing import TYPE_CHECKING
from Options import Toggle, Choice, PerGameCommonOptions, Range
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
class ScoreForLastCheck(Range):
    """The score of the last check in the slot."""
    display_name = "Final Check Score"
    range_start = 500
    range_end = 1500
    default = 800
class ScoreForGoal(Range):
    """The score needed to goal the slot."""
    display_name = "Goal Score"
    range_start = 500
    range_end = 1500
    default = 600
class CheckDensity(Range):
    """The density of locations in the slot."""
    display_name = "Check Density"
    range_start = 1
    range_end = 15
    default = 3
class ImportantItems(Choice):
    """The quantity of important items in the slot."""
    display_name = "Important Items"
    option_minimal = 1
    option_sparse = 2
    option_filled = 3
    option_overloaded = 4
    default = 2
@dataclass
class HighRollerOptions(PerGameCommonOptions):
    difficulty: Difficulty
    max_score: ScoreForLastCheck
    goal_score: ScoreForGoal
    check_density: CheckDensity
    crit_items: ImportantItems