import tileLayer

class TileMap:
    
    def __init__(self, mapData):
        self.mapData = mapData
        self.dimensions = mapData["dimensions"]
        # build layers
        self.groundLayer = tileLayer.GroundLayer(mapData)
        self.entityLayer = tileLayer.EntityLayer(mapData)
    
    def initialize_entities(self):
        self.entityLayer.spawn_player()
        self.entityLayer.load_entity_data()
        self.entityLayer.spawn_entities()
    
    def update(self):
        self.entityLayer.update()
    
    def draw(self):
        # only displays entityLayer for this program
        drawnMap = self.entityLayer.draw()
        for row in range(self.dimensions[0]):
            print(drawnMap[row])

# -----------------------setters & getters--------------------------

    def set_game_ref(self, game):
        self.game = game

    def set_player_ref(self, player):
        self.player = player
        self.entityLayer.set_player_ref(self.player)

    def get_matrix(self):
        return self.matrix
    
    def get_matrix_dimensions(self):
        return self.dimensions
    
    def get_entity_matrix(self):
        return self.entityLayer.matrix