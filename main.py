from ursina import *
from intro import StartGame#import self created class for main_menu options
class Game:
    def __init__(self):
        print('init was called.............................................')
        # Set the initial state for the state manager
        #self.state = 'main_menu'
        #set the variable for the method StartGame()
        self.start_game = StartGame()

    #initialize the main_menu method
    #def state_manager(self):
    #    if self.state == 'main_menu':
    #        self.main_menu()
    
    #run the start game class in the intro tab to select an intro button option
    def main_menu(self):
        self.StartGame()

if __name__ == '__main__':#run all code through this file in ursina
    app = Ursina()        #this is required to prevent multiple show bases
    game = Game()
    app.run()
    
  
