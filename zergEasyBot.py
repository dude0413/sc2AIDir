import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer
from sc2.constants import HATCHERY, LARVA, QUEEN, DRONE,
import random

# Setup Game Variables #
race = Race.Zerg
enemy_race = Race.Protoss
enemy_difficulty = Difficulty.Easy
realtime_condition = False
map_name = "AbyssalReefLE"
replay_name = "ZvTEasyFirst.SC2Replay"

class MitchyBot(sc2.BotAI):
 
    def __init__(self): 
        self.ITERATIONS_PER_MINUTE = 165
        self.MAX_WORKERS = 50
     
async def on_step(self, iteration):
        self.iteration = iteration
        await self.distribute_drones()
        await self.build_drones()
        await self.expand()
        await self.offensive_force_buildings()
        await self.build_offensive_force()
        await self.attack()
        
async def build_drones(self):
        if (len(self.units(HATCHERY)) * 16) > len(self.units(DRONE)) and len(self.units(DRONE)) < self.MAX_WORKERS:
            for h in self.units(HATCHERY).ready.noqueue:
               if self.can_afford(DRONE):
                  await self.do(h.train(DRONE))
sc2.run_game(sc2.maps.get(map_name), [
        Bot(race, MitchyBot()),
        Computer(enemy_race, enemy_difficulty)
    ], realtime=realtime_condition, save_replay_as=replay_name)
