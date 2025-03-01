import guard

class Submenu:
    def set_player_ref(self, player):
        self.player = player
    def select(self):
        pass
    def iterate(self):
        pass
    def draw(self):
        pass

class Stats(Submenu):
    def draw(self):
        for key in self.player.generalStats:
            print(key + ": " + str(self.player.generalStats[key]))
        for key in self.player.combatStats:
            print(key + ": " + str(self.player.combatStats[key]))

class Inventory(Submenu):
    def draw(self):
        print("(under construction. press m to exit)")

class Equipments(Submenu):
    def draw(self):
        print("(under construction. press m to exit)")