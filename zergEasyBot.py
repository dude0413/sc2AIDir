import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer
from sc2.constants import NEXUS, PROBE, PYLON, ASSIMILATOR, GATEWAY, \
 CYBERNETICSCORE, STALKER, STARGATE, VOIDRAY
import random

# Setup Game Variables #
race = Race.Zerg
enemy_race = Race.Protoss
enemy_difficulty = Difficulty.Easy
realtime_condition = False
map_name = "AbyssalReefLE"

class MitchyBot(sc2.BotAI):
 
    def __init__(self): 
        self.ITERATIONS_PER_MINUTE = 165
        self.MAX_WORKERS = 50
     
async def on_step(self, iteration):
        self.iteration = iteration
        await self.distribute_workers()
        await self.build_workers()
        await self.expand()
        await self.offensive_force_buildings()
        await self.build_offensive_force()
        await self.attack()
