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
    
    def set_game_ref(self, game):
        for state in self.keyToState.values():
            state.set_game_ref(game)

    def handle_input(self):
        newState = self.state.handle_input()
        if newState != None:
            self.state = self.keyToState[newState]
            self.state.enter()

    # when a state change happens outside of gamestate
    def set_state(self, newState):
        self.state = self.keyToState[newState]
        self.state.enter()
    
    def draw(self):
        self.state.draw()