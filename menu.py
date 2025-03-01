import guard
import submenu

class Menu:
    def __init__(self):
        self.stats = submenu.Stats()
        self.equipments = submenu.Equipments()
        self.inventory = submenu.Inventory()
        self.submenus = [
            "stats",
            "equipments",
            "inventory"
        ]
        self.keyToSubmenu = {
            "stats": self.stats,
            "equipments": self.equipments,
            "inventory": self.inventory
        }
        self.currentIndex = 0
        self.submenu = None

    def exit(self):
        if self.submenu == None:
            self.game.set_state("map")
            self.currentIndex = 0
        else:
            self.submenu = None
            
    def select(self):
        if self.submenu == None:
            key = self.submenus[self.currentIndex]
            self.submenu = self.keyToSubmenu[key]
        else:
            self.submenu.select()

    def iterate(self, input):
        keyToValue = {
            "w": -1,
            "s": 1
        }
        if guard.against_menu_out_of_bounds(self.currentIndex, len(self.submenus), keyToValue[input]) == True:
            if self.submenu == None:
                self.currentIndex += keyToValue[input]
            else:
                self.submenu.iterate()
            
    def draw(self):
        if self.submenu == None:   
            for item in self.submenus:
                if self.submenus.index(item) == self.currentIndex:
                    print("▷ " + item)
                else:
                    print(item)
        else:
            self.submenu.draw()

# -----------------------setters--------------------------

    def set_game_ref(self, game):
        self.game = game

    def set_player_ref(self, player):
        for submenu in self.keyToSubmenu.values():
            submenu.set_player_ref(player)