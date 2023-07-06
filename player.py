from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from direct.actor.Actor import Actor

class Player(FirstPersonController):
    def __init__(self):
        print('firstpersoncroller got called -=====================================')
        #moveforwards = 'model'
        super().__init__(#model = 'anime',
                                    position = (0,3,0),
                                    speed=30,
                                    origin=(0,0,-2),
                                    scale=(7),
                                    color=color.peach,collider='box',#rotation_z=180,
                                    health=100,
                                    )
        print('firstpersoncroller got called -=====================================')
        self.ghostPerson = Entity(parent=self, position = (0,0,2), rotation_y = 180)
        #self.moveRight.enabled = False

    def doubleSpeed(self):
        self.original_speed = self.speed
        self.speed *= 2
    #animationModel has movement in it 4/29/23
    def moveForward(self):
        self.player_model = "assets/Jinx.gltf"

        self.actor = Actor(self.player_model)
        self.actor.reparent_to(self.ghostPerson)

        self.actor.loop("JinxRigAction.1")
        #invoke(self.check_animation_finished, delay=self.actor.play("movement"))#.length)

        #self.actor = Actor("assets/Jinx.gltf")
        ##self.actor.texture = None
        #self.actor.reparent_to(self.ghostPerson)

        #self.actor.loop("JinxRigAction.1")
    def moveLeft(self):
        #self.actor = Actor("animationModel.glb")  # change filename to the GLB file
        #self.actor.reparent_to(self.ghostPerson)

        #self.actor.play("moveLeft")

        while True: #doesn't exist yet
            self.actor = Actor("anime.glb")  # change filename to the GLB file
            self.actor.reparent_to(self.ghostPerson)

            self.actor.play("moveLeft")
            while self.actor.animations['moveLeft'].loop or self.actor.animations['moveLeft'].playing:
                yield

    #def input(key, self):
        #if key == 'a':
        #    self.moveRight.enabled = True
        #invoke(self.check_animation_finished)#, delay=self.actor.play("movement"))#.length)

    
    #def check_animation_finished(self):
    #    if not self.actor:
    #        destroy(self.moveRight)
    #        return

    #    # perform some action here when animation finishes
    #    print("Animation finished!")

        # remove ghostPerson and actor from the scene
        #self.ghostPerson.enabled = False 
        #self.actor.enabled = False

