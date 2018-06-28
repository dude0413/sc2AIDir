import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer
from sc2.constants import NEXUS, PROBE, PYLON, ASSIMILATOR, GATEWAY, \
 CYBERNETICSCORE, STALKER, STARGATE, VOIDRAY
import random

# Setup Game Variables #
race = Race.Protoss
enemy_race = Race.Terran
enemy_difficulty = Difficulty.Hard
realtime_condition = False
map_name = "AbyssalReefLE"
