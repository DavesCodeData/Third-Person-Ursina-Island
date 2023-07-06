from ursina import *
#from ursina.prefabs.frame_animation_3d import FrameAnimation3d
from direct.actor.Actor import Actor
from player import Player

class Mob(Entity):
    def __init__(self):
        super().__init__(#model='anime',        #self.person = Entity
                                  color= color.peach,
                                  origin_y=0.5,
                                  collider='box',
                                  scale=7,
                                  position = (0,10,20),
                                  double_sided=True,
                                  animation_speed=0.2, 
                                  )
        #self.player = Player()
        #self.target = self.player
        #self.player.enabled = False
        #self.target.enabled = False
    def action(self):
        self.actor = Actor("assets/anime.glb")  # change filename to the GLB file
        self.actor.reparent_to(self)
        self.actor.play("moveForward")

    #def follow(self):
    #    self.player.enabled = True
    #    self.target.enabled = True
    #    self.add_script(SmoothFollow(target=self.target,
    #                                            #offset = [0,3,0],
    #                                            #offset = [0,3,-10],
    #                                            speed =0.5)
    #                            )
        #self.actor = Actor("model.glb")  # change filename to the GLB file
        #self.actor.reparent_to(self.mob)

        #self.actor.play("movement")
        #self.rotation = Vec3(0,self.rotation.y+180,0)
        #self.person = FrameAnimation3d('')
        #self.person.position = Vec3(0,2,0)
        #self.player = Player()
        #model.look_at(camera.position)

    #def mob_movement(self, person, playerposition):
    #    self.person.lookAt(playerposition, person.turnSpeed * time.dt)

    #    self.mob.enabled = False
    #    self.speed=30
    #    self.target = None

    #def update(self):
    #    if self.target is None:
    #        self.mob.enabled = True
    #        direction = self.target.position - self.position
    #        distance = direction.length()
    #        if distance < 5:
    #            print('Enemy attacks player!')
    #            # add code here to perform an attack on the player
    #        else:
    #            self.position += direction.normalized() * self.speed * time.dt

    ##def mob(self):
    ##    self.mob.enabled = True

