from sc2.bot_ai import BotAI


class WorkerRushBot(BotAI):
    async def on_step(self, iteration):
        if iteration == 0:
            for worker in self.workers:
                worker.attack(self.enemy_start_locations[0])
