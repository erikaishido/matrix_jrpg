import json
import entity

class TileLayer:
    def __init__(self, mapData):
        self.mapData = mapData
        self.dimensions = mapData["dimensions"]
        self.rows = self.dimensions[1]
        self.cols = self.dimensions[0]
        self.matrix = [[0 for x in range(self.rows)] for y in range(self.cols)]
    def set_player_ref(self, player):
        self.player = player

class GroundLayer(TileLayer):
    pass

class EntityLayer(TileLayer):
    def spawn_player(self):
        playerCoords = self.mapData["playerSpawnCoords"]
        self.set_player_coords(playerCoords)

    def load_entity_data(self):
        npcFile = open("npcData.json")
        self.allNpcData = json.load(npcFile)
        npcFile.close()

    def spawn_entities(self):
        # spawn npcs
        npcs = self.mapData["npcs"]
        for each in npcs:
            id = each[0]
            coords = each[1]
            npcData = self.allNpcData[id]
            thisNpc = entity.Npc(npcData)
            self.matrix[coords[0]][coords[1]] = thisNpc
        # spawn warpzones
        warpzones = self.mapData["warpzones"]
        for each in warpzones:
            destination = each[0]
            coords = each[1]
            thisWarp = entity.Warpzone(destination)
            self.matrix[coords[0]][coords[1]] = thisWarp
    
    def update(self):
        last = self.player.lastCoords
        new = self.player.coords
        self.matrix[last[0]][last[1]] = 0
        self.matrix[new[0]][new[1]] = self.player

    def draw(self):
        # make a new map for display
        # essentially replaces each object reference to its id
        drawnMap = [[0 for x in range(self.rows)] for y in range(self.cols)]
        for x in range(self.rows):
            for y in range(self.cols):
                if self.matrix[y][x] != 0:
                    entity = self.matrix[y][x]
                    drawnMap[y][x] = entity.get_id()
        return drawnMap 

    def set_player_coords(self, coords):
        self.matrix[coords[0]][coords[1]] = self.player
