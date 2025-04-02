import gameState

class StateMachine:

    def __init__(self):
        self.mapState = gameState.MapState()
        self.menuState = gameState.MenuState()
        self.keyToState = {
            "map": self.mapState,
            "menu": self.menuState
        }
        self.state = self.mapState
    
# -----------------------game loop--------------------------

    def handle_input(self):
        self.state.handle_input()
    
    def update(self):
        self.state.update()
        # check for new state
        newState = self.state.get_new_state()
        if newState != None:
            self.state.exit()
            self.state = self.keyToState[newState]
            self.state.enter()

    def draw(self):
        self.state.draw()

# -----------------------getters & setters--------------------------

    def set_game_ref(self, game):
        for state in self.keyToState.values():
            state.set_game_ref(game)
    
    # when a state change happens outside of gamestate
    def set_state(self, newState):
        self.state = self.keyToState[newState]
        self.state.enter()