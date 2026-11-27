from dataclasses import dataclass
import pickle
from pathlib import Path
from typing import TYPE_CHECKING
from Options import OptionError
if TYPE_CHECKING:
    from .world import StrawberryJamWorld
    from .options import StrawberryJamOptions


@dataclass
class MapData:
    SID: str
    name: str
    difficulty: int
    difficulty_name: str
    heartside: bool

    @classmethod
    def from_dict(cls, data: dict):
        sid = data["Map File Name"]
        name = data["Stylized Map Name"]
        difficulty = data["Difficulty"]
        difficulty_name = data["Difficulty Color"]
        heartside = data["Heartside"]
        return cls(sid, name, difficulty, difficulty_name, heartside)


class Maps:
    difficulty_color_to_int = {
        "Beginner Green": 1,
        "Beginner Yellow": 2,
        "Beginner Red": 3,
        "Intermediate Green": 4,
        "Intermediate Yellow": 5,
        "Intermediate Red": 6,
        "Advanced Green": 7,
        "Advanced Yellow": 8,
        "Advanced Red": 9,
        "Expert Green": 10,
        "Expert Yellow": 11,
        "Expert Red": 12,
        "Grandmaster Green": 13,
        "Grandmaster Yellow": 14,
        "Grandmaster Red": 15,
        "Grandmaster Cracked Red": 16
    }

    lobby_to_difficulty_colors = {
        "Beginner": [1, 2, 3],
        "Intermediate": [4, 5, 6],
        "Advanced": [7, 8, 9],
        "Expert": [10, 11, 12],
        "Grandmaster": [13, 14, 15, 16],
    }

    lobby_to_heartside_difficulty = {
        "Beginner": 4,
        "Intermediate": 7,
        "Advanced": 10,
        "Expert": 13,
        "Grandmaster": 17
    }

    def __init__(self):
        self.enabled_maps = []
        map_ids_path = Path(__file__).parent.resolve() / "data" / "SJArchiepalgoTables - MapIDs.pickle"
        with open(map_ids_path, 'rb') as file:
            self.map_data = pickle.load(file)
        self.map_data = {i: MapData.from_dict(j) for i, j in self.map_data.items()}


    def get_enabled_maps(self, world: StrawberryJamWorld):
        if len(self.enabled_maps) > 0:
            return {i.sid for i in self.enabled_maps}

        difficulties_to_exclude = set()
        maps_to_exclude = list()
        heartsides_to_exclude = set()
        options : StrawberryJamOptions = world.options

        # first, remove based on lobbies by adding to difficulties to exclude
        lobbies = set(self.lobby_to_difficulty_colors.keys())
        lobbies_to_exclude = lobbies - options.lobbies.value
        for lobby in lobbies_to_exclude:
            heartsides_to_exclude.add(self.lobby_to_heartside_difficulty[lobby])
            difficulties_to_exclude.update(set(self.lobby_to_difficulty_colors[lobby]))

        # next, add the excluded difficulties
        difficulties_to_exclude.update({self.difficulty_color_to_int[i] for i in options.exclude_difficulties.value})

        # then, convert the difficulties to maps.
        for mapdata in self.map_data.values():
            if not mapdata.heartside:
                if mapdata.difficulty in difficulties_to_exclude:
                    maps_to_exclude.append(mapdata)
                continue

            # heartside logic
            if mapdata.difficulty in heartsides_to_exclude:
                maps_to_exclude.append(mapdata)

        # exclude maps based on lobbies and difficulties
        excluded_sids = {i.SID for i in maps_to_exclude}
        self.enabled_maps = [i for i in self.map_data.values() if i.SID not in excluded_sids]

        # exclude maps based on exclude maps option
        option_map_exclusion_set = options.exclude_maps.value
        self.enabled_maps = [i for i in self.enabled_maps if i.name not in option_map_exclusion_set]

        # now we need some cleanup.
        # heartside difficulties need to be changed to the next highest difficulty in the enabled difficulties list.
        enabled_difficulties_set = {i.difficulty for i in self.enabled_maps if not i.heartside}

        # i swear 0 should never not be in this set but just in fucking case OIGHQRIUORGHEQOIU INM LOISUIGNGG ITTTTT
        # AAAAAAAAYUWDFGUYADGFISUDAGHIUASDHGOIUDASFGH
        # WHO MADE THIS FUNCTION SO HARD TO WRITE
        enabled_difficulties_set.add(0)
        enabled_difficulties = list(enabled_difficulties_set)
        enabled_difficulties.sort()

        enabled_heartsides = [i for i in self.enabled_maps if i.heartside]
        if len(enabled_heartsides) < 1 and (
                options.goal_condition.value == options.goal_condition.option_all_heartsides or
                options.goal_condition.value == options.goal_condition.option_final_heartside):
            raise OptionError("No enabled heartsides found. The goal set requires at least one enabled heartside.")

        return self.enabled_maps

