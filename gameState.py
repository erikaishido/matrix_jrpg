import guard

class State:
    def __init__(self):
        pass
    def set_game_ref(self, game):
        self.game = game
    def enter(self):
        pass
    def handle_input(self):
        pass
    def draw(self):
        pass
        

class MapState(State):
    def __init__(self):
        self.moveKeys = {"w", "a", "s", "d"}
        self.interactKeys = {"x"}
        self.menuKeys = {"m"}
        self.validKeys = self.moveKeys.union(self.interactKeys, self.menuKeys)

    def enter(self):
        print("enter map")

    def handle_input(self):
        userInput = input("\nwasd to move: ")
        if guard.against_invalid_key_input(userInput, self.validKeys) == True:
            if userInput in self.menuKeys:
                return "menu"
            elif userInput in self.moveKeys:
                self.game.move_player(userInput)
            elif userInput in self.interactKeys:
                self.game.player_interact()
        
    def draw(self):
        self.game.draw_map()

class MenuState(State):
    def __init__(self):
        self.upDownKeys = {"w", "s"}
        self.selectKey = {"x"}
        self.exitKey = {"m"}
        self.validKeys = self.upDownKeys.union(self.selectKey, self.exitKey)

    def enter(self):
        #print("enter menu")
        pass

    def handle_input(self):
        userInput = input("\nws to navigate menu, x to select: ")
        if guard.against_invalid_key_input(userInput, self.validKeys) == True:
            if userInput in self.exitKey:
                self.game.exit_menu()
                #return "map"
            elif userInput in self.upDownKeys:
                self.game.iterate_menu(userInput)
            elif userInput in self.selectKey:
                self.game.select_menu()
    
    def draw(self):
        self.game.draw_menu()