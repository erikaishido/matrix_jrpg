import tileMap
import json
import stateMachine
import utilities
import entity
import menu
import guard

class Game:
    
    def __init__(self):
        # set up player
        self.player = entity.Player()
        self.load_player_data()
        # set up map
        self.map = self.load_map("map001")
        self.map.set_game_ref(self)
        self.map.set_player_ref(self.player)
        self.map.initialize_entities()
        # set up menu
        self.menu = menu.Menu()
        self.menu.set_player_ref(self.player)
        self.menu.set_game_ref(self)
        # set up others
        self.stateMachine = stateMachine.StateMachine()
        self.stateMachine.set_game_ref(self)
        # draw map to start
        self.draw_map()

# -----------------------load files--------------------------

    def load_player_data(self):
        # load stats from json
        file = open("playerData.json")
        data = json.load(file)
        file.close()
        # give states to player
        self.player.set_initial_stats(data)
        
    def load_map(self, mapId):
        # load map from json
        file = open("mapData.json")
        allMapData = json.load(file)
        mapData = allMapData[mapId]
        file.close()
        # create map
        map = tileMap.TileMap(mapData)
        return map
    
# -----------------------input--------------------------

    def handle_input(self):
        self.stateMachine.handle_input()

# -----------------------statemachine functions--------------------------

    def set_state(self, newState):
        self.stateMachine.set_state(newState)

# -----------------------player move/interact--------------------------

    def move_player(self, key):
        keyToCoords = {
            "w": [-1,0],
            "a": [0,-1], 
            "s": [1,0], 
            "d": [0,1]
        }
        newCoords = utilities.sum_coords(self.player.get_coords(), keyToCoords[key])
        matrixSize = self.map.get_matrix_dimensions()
        if guard.against_matrix_out_of_bounds(newCoords, matrixSize) == True:
            entityMatrix = self.map.get_entity_matrix()
            if entityMatrix[newCoords[0]][newCoords[1]] != 0:
                print("there is something blocking your path...")
            else:
                self.player.set_coords(newCoords)

    def player_interact(self):
        modifiers = [[-1,0], [0,-1], [1,0], [0,1]]
        for mod in modifiers:
            adjacentTile = utilities.sum_coords(self.player.coords, mod)
            matrixSize = self.map.get_matrix_dimensions()
            if guard.against_matrix_out_of_bounds(adjacentTile, matrixSize) == True:
                entity = self.check_for_entity(adjacentTile)
                if entity != None:
                    entity.interact()

    def check_for_entity(self, coords):
        matrix = self.map.get_entity_matrix()
        adjacent = matrix[coords[0]][coords[1]]
        if adjacent != 0:
            return adjacent
        
# -----------------------menu functions--------------------------

    def exit_menu(self):
        self.menu.exit()
    def iterate_menu(self, input):
        self.menu.iterate(input)
    def select_menu(self):
        self.menu.select()
        
# -----------------------update--------------------------

    def update(self):
        self.map.update()

# -----------------------draw--------------------------

    def draw(self):
        self.stateMachine.draw()
    def draw_map(self):
        self.map.draw()
    def draw_menu(self):
        self.menu.draw()
    
# -----------------------main--------------------------

def main():
    game = Game()
    while(True):
        game.handle_input()
        game.update()
        game.draw()

if __name__ == '__main__':
    utilities.clearScreen()
    main()
