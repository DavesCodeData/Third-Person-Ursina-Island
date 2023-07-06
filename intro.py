from ursina import *
from level import MainScene #import the game from level file class MainScene
class StartGame():#intro class
    def __init__(self, **kwargs):
        #super().__init__
        self.button=Button(#first button built in method Button
            text='Start',
            color=color.black,
            highlight_color=color.red,
            pressed_color=color.green,
            scale=(0.2, 0.15),
            position=(0, -.15),
            **kwargs
        )
        self.button.on_click = self.on_button_click#set the self parameter to a button click

        self.button2=Button(text='Exit',#second button built in method Button
            color=color.black,
            highlight_color=color.red,
            pressed_color=color.green,
            scale=(0.2, 0.15),
            position=(0, -.40),
            **kwargs
        )
        self.button2.on_click = self.on_button2_click#set the self parameter to a button
        self.main_scene = MainScene()#create a variable for class MainScene() in level file
        self.menu = Entity(#create an built in Entity instance to display an image
        model='quad',
        texture='MenuScreen.png',
        scale=(7, 3.5, 3.5),
        position=(0, 0, -15),
        origin=(0, 0, 0)
        )
        self.text = Text(text='MAD Island!', origin=(0, -1), scale=6)#display text
        self.text.y = 0.1
                   
    def on_button_click(self):#first button called from on_click method line 15
        print('Button1 clicked!================================================')
        try:#stay in the try loop

            for event in held_keys:
                if held_keys['left mouse']:                   
                    destroy(self.button)        #from level file class MainScene
                    destroy(self.button2)
                    destroy(self.text)
                    destroy(self.menu)
                    self.main_scene.load_scene()#load in def load_scene
                if held_keys['escape']:#you can also press escape to kill program
                    sys.exit()
        except:
            pass

    def on_button2_click(self):#second button called from on_click method line 25
        print('Button2 clicked!================================================')
        try:#stay in the try loop

            for event in held_keys:
                if held_keys['left mouse']:
                    application.quit()#kill program
                if held_keys['escape']:#you can also press escape to kill program
                    sys.exit()
        except:
            pass





