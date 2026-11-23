from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, OptionSet


class Lobbies(OptionSet):
    """
    The lobbies that will be playable in the world. Options are:
    Beginner
    Intermediate
    Advanced
    Expert
    Grandmaster
    """
    display_name = "Lobbies to Include"
    valid_keys = {"Beginner", "Intermediate", "Advanced", "Expert", "Grandmaster"}
    default = {"Beginner", "Intermediate", "Advanced"}
    valid_keys_casefold = False


class ExcludeMaps(OptionSet):
    """
    The maps that you would like to exclude from the world. Enter any map name here.
    """
    display_name = "Excluded Maps"


class ExcludeDifficulties(OptionSet):
    """
    The difficulties that you would like to exclude from the world.
    This is meant to give you more granular control if you would like to play, for example, some of GM lobby, but not GM cracked reds.
    Options are:
    Beginner[Green/Yellow/Red]
    Intermediate[Green/Yellow/Red]
    Advanced[Green/Yellow/Red]
    Expert[Green/Yellow/Red]
    Grandmaster[Green/Yellow/Red/CrackedRed]
    """
    display_name = "Exclude Difficulties"
    valid_keys = {"BeginnerGreen", "BeginnerYellow", "BeginnerRed",
                  "IntermediateGreen", "IntermediateYellow", "IntermediateRed",
                  "AdvancedGreen", "AdvancedYellow", "AdvancedRed",
                  "ExpertGreen", "ExpertYellow", "ExpertRed",
                  "GrandmasterGreen", "GrandmasterYellow", "GrandmasterRed", "GrandmasterCrackedRed"}
    default = frozenset()
    valid_keys_casefold = False


class CatSanity(Choice):
    """
    The difficulty of cats that you would like to include as location checks. Options are:
    Standard - Nothing crazy for whatever lobbies you are playing.
    Grandmaster - Add Supernautica, Vinculum, Psychokinetic Cats.
    mrrrowww - Add ALL cats!!!! Includes both Call of the Void, Summit Down-Side, and both Ivory Cats.
    WARNING: mrrrrp is INCREDIBLY difficult. ONLY use this setting if you have gotten these cats before.
    """
    display_name = "Cat Sanity"
    valid_keys = ["Standard", "Grandmaster", "mrrrowww"]
    defauly = ["Standard"]
    valid_keys = False


@dataclass
class SJAPOptions(PerGameCommonOptions):
    lobbies: Lobbies
    exclude_maps: ExcludeMaps
    exclude_difficulties: ExcludeDifficulties
    cat_sanity: CatSanity


option_groups = [
    OptionGroup(
        "Gameplay Options",
        [],
    ),
    OptionGroup(
        "Aesthetic Options",
        [],
    ),
]
