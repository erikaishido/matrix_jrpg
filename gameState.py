import guard
import utilities

class State:
    def enter(self):
        print("entering " + self.name)
    def exit(self):
        self.newState = None
    def set_game_ref(self, game):
        self.game = game
    def get_new_state(self):
        return self.newState

# -----------------------------------------------------------------------------------

class MapState(State):
    def __init__(self):
        self.moveKeys = {"w", "a", "s", "d"}
        self.interactKeys = {"x"}
        self.menuKeys = {"m"}
        self.validKeys = self.moveKeys.union(self.interactKeys, self.menuKeys)
        self.name = "map"
        self.command = None
        self.newState = None
    
    def handle_input(self):
        userInput = input("\nwasd to move: ")
        if guard.against_invalid_key_input(userInput, self.validKeys) == True:
            self.command = userInput
    
    def update(self):
        if self.command != None:
            if self.command in self.menuKeys:
                self.newState = "menu"
            elif self.command in self.moveKeys:
                utilities.clearScreen()
                self.game.move_player(self.command)
            elif self.command in self.interactKeys:
                utilities.clearScreen()
                self.game.player_interact()
            self.command = None

    def draw(self):
        self.game.draw_map()

# -----------------------------------------------------------------------------------

class MenuState(State):
    def __init__(self):
        self.upDownKeys = {"w", "s"}
        self.selectKey = {"x"}
        self.exitKey = {"m"}
        self.validKeys = self.upDownKeys.union(self.selectKey, self.exitKey)
        self.name = "menu"
        self.command = None
        self.newState = None

    def handle_input(self):
        userInput = input("\nws to navigate menu, x to select: ")
        if guard.against_invalid_key_input(userInput, self.validKeys) == True:
            self.command = userInput
    
    def update(self):
        if self.command != None:
            if self.command in self.exitKey:
                self.game.exit_menu()
                self.newState = "map"
            elif self.command in self.upDownKeys:
                self.game.iterate_menu(self.command)
            elif self.command in self.selectKey:
                self.game.select_menu()
            self.command = None
    
    def draw(self):
        utilities.clearScreen()
        self.game.draw_menu()