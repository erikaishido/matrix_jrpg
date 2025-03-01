class Entity:
    def __init__(self):
        pass
    def interact(self):
        pass
    def get_coords(self):
        return self.coords
    def get_id(self):
        return self.id

class Player(Entity):
    def __init__(self):
        self.id = 1
        self.coords = [0,0]
        self.lastCoords = self.coords
    def set_initial_stats(self, data):
        self.generalStats = data["general"]
        self.combatStats = data["combat"]
    def set_coords(self, newCoords):
        self.lastCoords = self.coords
        self.coords = newCoords

class Npc(Entity):
    def __init__(self, data):
        self.id = 2
        self.name = data["name"]
        self.dialogue = data["dialogue"]
    def interact(self):
        print(self.name + ": " + self.dialogue)

class Item(Entity):
    pass

class Warpzone(Entity):
    def __init__(self, destination):
        self.id = 4
        self.destination = destination
    def interact(self):
        print("(hi i'm supposed to be a functioning warpzone)")