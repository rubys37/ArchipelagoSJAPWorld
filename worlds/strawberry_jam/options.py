from dataclasses import dataclass

from Options import Toggle, Choice, Range, OptionGroup, PerGameCommonOptions, OptionSet


class GoalCondition(Choice):
    """
    The goal for the archipelago. Options:
    Heartside: Complete a specified heartside. 
    (planned) AllHeartsides: Complete all enabled heartsides.
    """
    display_name = "Goal Condition"
    option_final_heartside = 0
    option_all_heartsides = 1
    default = option_final_heartside


class GoalHeartside(Choice):
    """
    Specify the goal heartside. Only affects anything if you have goal condition set to 'Heartside' or 'AllHeartsides'.
    If you set this to a heartside from a lobby that has 0 playable maps, generation will fail.
    """
    display_name = "Goal Heartside"
    option_blueberry_bay = 0
    option_raspberry_roots = 1
    option_mango_mesa = 2
    option_starfruit_supernova = 3
    option_passionfruit_pantheon = 4
    default = option_mango_mesa


class RequiredHeartsForHeartside(Range):
    """
    Specify the number of hearts to unlock the heartsides.
    Only heartsides required for goal are locked by lobby hearts. Otherwise, they are locked with progressive difficulty equal to 1 greater than the hardest map in the lobby.
    If this is set higher than the number of maps in the lobby and lobby heart randomization is turned off, then this option will be overwritten with the max number of hearts in the lobby.
    Beginner has 21 hearts.
    Intermediate has 18 hearts.
    Advanced has 25 hearts.
    Expert has 29 hearts.
    Grandmaster has 18 hearts.
    """
    display_name = "Required Hearts To Unlock Heartside"
    range_start = 1
    range_end = 50


class RandomizeRequiredHearts(Toggle):
    """
    Turn on heart items to unlock the required hearts for your heartside goal.
    If this setting is disabled, all required hearts will be at their normal locations (at the end of maps).
    For example, if Expert HS is your goal, then turning this setting on means required expert hearts will be placed in the item pool.
    Turning it off means that expert hearts will be placed at the end of expert maps.
    """
    display_name = "Randomize Required Hearts"


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
    valid_keys = {['Prologue', 'Library', 'ForestPath', 'Driveway', 'AzureCaverns', 'CassetteCliffs', 'Soap', 'LoopyLagoon', 'OvertheCity', 'Troposphere', 'SwitchtubeVista', 'PotentialforAnything', 'AGiftFromtheStars', 'CollapsingSkyline', 'StrawberryOrchard', 'MidnightSpire', 'paint', 'SeeingisBelieving', 'Dropzle', 'RoseGarden', 'Treehive', 'TheSqueeze', 'CoresakenCity', 'BlueberryBay', 
                   'SleepingUnderStars', 'SquaretheCircle', 'FrostedFragments', 'DeepBlue', 'Vertigo', 'EATGIRL', 'HoneyzipInc', 'Templeofathousandskies', 'InFiltration', 'Supernautica', 'FifthDemension', 'MidnightMonsoon', 'LowGBotany', 'TheTower', 'PufferfishTransportationCo', 'SeaofSoup', 'ConstructionConundrum', 'PointlessMachines', 'RaspberryRoots', 
                   'SandsofTime', 'JellyfishSanctum', 'ToggleTheory', 'SlimeTime', 'Superstructure', 'LethalLaserLaboratory', 'StarryRuins', 'TheTowerXVI', 'StarlightStation', 'TectonicTrenches', 'GoldenDawn', 'DuskCity', 'ForestRush', 'Synapse', 'Undergrowth', 'LostWoods', 'AttackoftheClone', 'TheLab', "BelatedValentinesDay", 'ThinkingWithPortals', 'BeeBerserk', "JavasCrypt", 'RightsideDownCavern', 'CalloftheVoid', 'RaindropsonRoses', 'MangoMesa', 
                   'AChangeinDirection', 'FlyingBattery', 'SkylineUsurper', 'ChromaticComplex', 'FortressFall', 'TheCoreProblem', 'Psychokinetic', "GardenofKhutara", 'OvergrownLinn', 'Clockwork', 'PlasmaReactor', 'NarrowHollow', 'Hydroshock', 'FloatingPoint', 'StormRunner', 'SummitDown-Side', 'TimeTrouble', 'SubwayNeon', 'Hypnagogia', 'MeaninglessContraptions', 'EtherealAscension', 'Vinculum', 'GoldenAlleyway', 'MosaicGarden', 'SystemInvalidMapException', 'LunarPagoda', 'CaperCavortion', 'MadelineTheBubble', 'Polaris', 'StarfruitSupernova', 
                   'Superluminary', 'BellyoftheBeast', 'WorldAbyss', 'CycleMadnessBSide', 'StellarOdyssey', '74', 'Shattersong', 'Ivory', 'summit', 'PinballPurgatory', 'CaveoftheCrimsonSky', 'TheSolarExpress', 'FlipsideCliffside', 'LavaLayer', 'kevintechspam', 'Nelumbo', 'DriftingDeep', 'FracturedIridescence', 'PassionfruitPantheon']}


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


class RandomizeVanillaItems(Toggle):
    """
    Choose if you want to randomize vanilla items.
    Enabling this locks all vanilla items and requires you to get the associated item before unlocking the item.
    Generation note: This HIGHLY increases the chance of sphere 1 being heavily restricted, which means generation fails can occur.
    Only use this setting if you are okay with that risk.
    """


class MapRando(Choice):
    """
    Choose if you want to randomize map entrances.
    Map Rando is an option that randomizes the locations of entrances to maps. 
    For example, if both grandmaster lobby and beginner lobby are enabled, the entrance to Pinball Purgatory could be placed at the normal location to enter Azure Caverns.
    This will only randomize maps that are enabled.
    Options:
    None: All maps will be at their default locations.
    MainMaps: All enabled maps will be shuffled.
    Gyms: All enabled maps and gyms will be shuffled.
    Heartsides: All enabled maps and heartsides will be shuffled.
    GymsHeartsides: All enabled maps, gyms, and heartsides will be shuffled.
    """
    display_name = "Map Randomization"


class CatSanity(Choice):
    """
    The difficulty of cats that you would like to include as location checks. Options are:
    Standard - Nothing crazy for whatever lobbies you are playing.
    Grandmaster - Add Supernautica, Vinculum, Psychokinetic Cats.
    mrrrowww - Add ALL cats!!!! Includes both Call of the Void, Summit Down-Side, and both Ivory Cats.
    WARNING: mrrrrp is INCREDIBLY difficult. ONLY use this setting if you have gotten these cats before.
    """
    display_name = "Cat Sanity"
    option_none = 0
    option_standard = 1
    option_grandmaster = 2
    option_mrrrowww = 3
    default = option_standard


class GymSanity(Toggle):
    """
    Whether to enable gym locations for enabled lobbies.
    
    """
    display_name = "Gym Sanity"


class SilverSanity(Choice):
    """
    The difficulty of silvers that you would like to include as locations checks. Options are:
    None
    Beginner[Green/Yellow/Red]
    Intermediate[Green/Yellow/Red]
    Advanced[Green/Yellow/Red]
    Expert[Green/Yellow/Red]
    Grandmaster[Green/Yellow/Red/CrackedRed]
    """
    display_name = "Silver Sanity"
    option_none = 0
    option_beginner_green = 1
    option_beginner_yellow = 2
    option_beginner_red = 3
    option_intermediate_green = 4
    option_intermediate_yellow = 5
    option_intermediate_red = 6
    option_advanced_green = 7
    option_advanced_yellow = 8
    option_advanced_red = 9
    option_expert_green = 10
    option_expert_yellow = 11
    option_expert_red = 12
    option_grandmaster_green = 13
    option_grandmaster_yellow = 14
    option_grandmaster_red = 15
    option_grandmaster_cracked_red = 16
    option_grandmaster_plus_one_green = 17
    default = option_none


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
