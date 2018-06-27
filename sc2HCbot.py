import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer
from sc2.constants import NEXUS, PROBE, PYLON, ASSIMILATOR


class MitchyBot(sc2.BotAI):
    # For every iteration, do the following (if the conditions are met): #
    async def on_step(self, iteration):
        await self.distribute_workers()  # in sc2/bot_ai.py
        await self.build_workers()  # build some of dem workers
        await self.build_pylons()  # build supply buildings
        await self.expand()  # expand to a new resource area.
        await self.build_assimilator()  # getting gas

    """ Build Workers:
    LLogic: If a Nexus has no queue and we can afford them, create some probes """
    async def build_workers(self):
        # nexus = command center
        for nexus in self.units(NEXUS).ready.noqueue:
            # we want at least 20 workers, otherwise let's allocate 70% of our supply to workers.
            # later we should use some sort of regression algo maybe for this?

            if self.can_afford(PROBE):
                await self.do(nexus.train(PROBE))
    
    """ Build Pylons:
    Logic: """
    async def build_pylons(self):
        if self.supply_left < 5 and not self.already_pending(PYLON):
            nexuses = self.units(NEXUS).ready
            if nexuses.exists:
                if self.can_afford(PYLON):
                    await self.build(PYLON, near=nexuses.first)
    
    """ Expand:
    Logic: If we have less than 2 Nexuses and we can afford another, 
    use the default expand_now() function (expand to a nearby resource area)."""
    async def expand(self):
        if self.units(NEXUS).amount < 2 and self.can_afford(NEXUS):
            await self.expand_now()
    
    """ Build Assimilators:
    Logic: For every ready Nexus, if we can afford an assimilator, build it to a 
    vespene gas that is closer than 25 units away."""
    async def build_assimilator(self):
        for nexus in self.units(NEXUS).ready:
            vaspenes = self.state.vespene_geyser.closer_than(25.0, nexus)
            for vaspene in vaspenes:
                if not self.can_afford(ASSIMILATOR):
                    break
                worker = self.select_build_worker(vaspene.position)
                if worker is None:
                    break
                if not self.units(ASSIMILATOR).closer_than(1.0, vaspene).exists:
                    await self.do(worker.build(ASSIMILATOR, vaspene))


run_game(maps.get("AbyssalReefLE"), [
    Bot(Race.Protoss, MitchyBot()),
    Computer(Race.Terran, Difficulty.Easy)
], realtime=False)
