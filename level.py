from ursina import *
from direct.actor.Actor import Actor
from ursina.shaders import colored_lights_shader
from ursina.prefabs.health_bar import HealthBar
from mob import Mob
#from player import Player
from thirdpersoncontroller import ThirdPersonController
from enemy import Enemy
class MainScene(Entity):#Entity built in Ursina method for objects in self created __init__ method
    def __init__(self):
        super().__init__(self)
        #__init__ method load scene and define level objects attributes, and ghost entity
        self.level = load_blender_scene(path=application.asset_folder,#built in method
                                        name='worldBridge')#file in assets
        self.level.Cube.texture="cobblestone_floor_07_diff_1k"
        self.level.Cube.collider = 'mesh'
        self.level.Cube.texture_scale = (2, 2)  # adjust texture size
        self.level.start_point.visible = False

        self.level.grass.color = color.green
        self.level.grass.double_sided = True

        self.level.water.color = color.blue

        self.level.terrain.texture="coast_sand_rocks_02_diff_1k"
        self.level.terrain.double_sided = True

        self.level.mesh_collider.collider = 'mesh'
        self.level.mesh_collider.visible = False

        self.level.bridge1.texture = "cracked_concrete_wall_diff_1k"
        self.level.bridge1.double_sided = True
        self.level.bridge1.texture_scale = (5, 5) 
        self.level.bridge1.collider = 'mesh'
        self.level.bridge.texture_scale = (40, 40)
        self.level.bridge.double_sided = True
        self.level.bridge.texture = "cracked_concrete_wall_diff_1k"
        self.level.bridge.collider = 'mesh'
    
        self.level.deathzone.texture = "rust_coarse_01_diff_1k"
        self.level.deathzone.collider = 'mesh'
        self.level.handrail1.texture = "cracked_concrete_wall_diff_1k"
        self.level.handrail1.collider = 'mesh'
        self.level.handrail2.texture = "cracked_concrete_wall_diff_1k"
        self.level.handrail2.collider = 'mesh'
        self.level.handrail3.texture = "cracked_concrete_wall_diff_1k"
        self.level.handrail3.collider = 'mesh'
        self.level.handrail4.texture = "cracked_concrete_wall_diff_1k"
        self.level.handrail4.collider = 'mesh'

        self.level.border.collider = 'mesh'
        self.level.waterborder.collider = 'mesh'
        self.level.waterborder.visible = False
        self.level.border.visible = False
        self.level.Circle.visible = False

        self.level.pillars.collider = 'mesh'
        #self.level.pillars.color = color.black
        self.level.pillars.texture = 'wood_table_001_diff_1k'
        self.level.pillars.texture_scale = (10, 10)  # adjust texture size
        self.level.roof.collider = 'mesh'
        self.level.roof.color = color.red
        self.level.roof.texture = 'roof_tiles_14_diff_1k'
        self.level.roof.texture_scale = (10, 10)  # adjust texture size
        #I could fix this in blender but I simply don't want to
        self.level.lightHouse1.collider = 'mesh'
        self.level.lightHouse1.texture = 'cobblestone_floor_07_diff_1k'
        self.level.lightHouse1.texture_scale = (5, 5)  # adjust texture size
        self.level.lightHouse1.double_sided = True
        self.level.lightHouse2.collider = 'mesh'
        self.level.lightHouse2.texture = 'rust_coarse_01_diff_1k'
        self.level.lightHouse2.double_sided = True
        self.level.lightHouse2.rotation_z = 360#I know it makes no sense
        self.level.lightHouse3.collider = 'mesh'
        self.level.lightHouse3.texture = 'rust_coarse_01_diff_1k'
        self.level.lightHouse3.rotation_z = 360
        self.level.lightHouse3.double_sided = True
        self.level.lightHouse4.collider = 'mesh'
        self.level.lightHouse4.texture = 'rust_coarse_01_diff_1k'
        self.level.lightHouse4.rotation_z = 360
        self.level.lightHouse4.double_sided = True

        self.level.bow.parent = camera
        self.level.bow.position = (.5,0,1)
        self.level.bow.enabled = False
        #self.level.bow.color = color.brown
        self.level.bow.shader = colored_lights_shader
        self.level.arrow.position = (.5,0,1)

        self.level.enemy.collider = 'mesh'
        self.textEnemy1 = Text('Shoot, here!', origin=(0, 0), position=(0, 10, 0),
                        parent=self.level.enemy, color=color.red, scale=90, rotation_y = 90)
        self.textEnemy1.enabled = True
        self.level.enemy2.collider = 'mesh'
        self.level.enemy2.enabled = False
        self.textEnemy2 = Text('Hit "c" to create an enemy!',
                        origin=(0, 0), position=(0, 3, 0),
                       parent=self.level.Cube, color=color.red, scale=20)
        self.textEnemy3 = Text('Shoot the cobble to move the gates',
                        origin=(0, 0), position=(0, 6, 0),
                       parent=self.level.Cube, color=color.red, scale=20)
        #self.level.lid.color = color.brown
        self.level.lid.collider = 'box'
        self.level.lid.texture = 'wood_floor_deck_diff_1k'
        self.level.lid.double_sided = True
        self.level.chest.texture = 'wood_floor_deck_diff_1k'
        #self.level.chest.color = color.brown
        self.level.chest.double_sided = True
        self.level.chest.collider = 'mesh'
        self.level.chest.on_click = self.combinedChestLidClick
        self.level.lid.on_click = self.combinedChestLidClick
        self.turnoffShader = True
        self.textChest = Text('Click, here!', origin=(0, 0), position=(0, 4, 0),
                        parent=self.level.chest, color=color.red, scale=30)
        

        self.level.gate1.texture = 'metal_plate_diff_1k'
        self.level.gate1.texture_scale = (10, 10)
        self.level.gate1.collider = 'mesh'
        self.level.gate2.texture = 'metal_plate_diff_1k'
        self.level.gate2.texture_scale = (10, 10)
        self.level.gate2.collider = 'mesh'

        self.enemyPlayer = Enemy()
        self.enemyPlayer.enabled = False

        self.pivot_point = Entity(parent=self.level.chest.parent,#ghost entity
                                  position=(0, -0.5, 3.7))#never change these numbers

        self.animeGirl = Entity(position=(4, 4, 4),
                        scale=(9, 9, 9),
                        double_sided=True,
                        animation_speed=0.2)

        self.HB1 = HealthBar(bar_color=color.red.tint(-.25), roundness=.5,)
        self.HB1.enabled = False#don't enable the health bar until the scene loads
        #self.myMob = Mob()
        self.timer = time.time() + 3 # set initial timer for 5 seconds
        self.startEnemyProgram = False
        self.mob = Mob()
        self.mob.enabled = False

        self.player = None

    def load_scene(self):
        self.turnOffShader = False
        #FirstPersonController built in Ursina method
        self.HB1.enabled = True#enable the health bar when the scene loads
        #self.player = Player()#call Player class in player file
        self.player = ThirdPersonController()#added on 5/24/23
        print('firstpersoncroller in load_scene -=====================================')
        self.target = self.player
        self.player.original_speed = self.player.speed
        #next line is not needed in a game this small but it clips with in the 
        #view frustrum to create a render distance
        camera.clip_plane_far = 600
        Sky(texture='castaway_sky', scale=camera.clip_plane_far-1)

    def combinedChestLidClick(self):
        if distance_xz(self.player.position, self.level.chest.position) < 30:
            self.on_chest_click()
            self.turnOffChestLights()

    def on_chest_click(self):
        if distance_xz(self.player.position, self.level.chest.position) < 30:
            self.level.lid.parent = self.pivot_point#Set the ghost pivot point as the parent of the lid
            self.level.lid.animate('rotation_x', self.level.lid.rotation_x + 120, duration=.2)
            invoke(setattr, self.level.bow, 'enabled', True, delay=.25)
            self.level.chest.on_click = None
            self.level.lid.on_click = None
            self.textChest.enabled = False

        #mechaninc key inputs and support
    def input(self, key):#registers key inputs new parameter (key)
        #if key == 'shift':
            #self.player.doubleSpeed()#double speed from class Player

        #elif key == 'shift up':
            #self.player.speed = self.player.original_speed

        if held_keys['control'] and key == 'r':#if you fall through mesh go back to starting point
            self.player.position = self.level.start_point.position

        if key == 'u':#go under the world
            self.player.position = (-4, -4, -4)

        if self.level.bow.enabled and key == 'left mouse down':
            self.player.arrow = duplicate(self.level.arrow, world_parent=self.level.bow, position=Vec3(-.2, 0, 0), rotation=Vec3(0, 0, 0))
            self.player.arrow.animate('position', self.player.arrow.position + Vec3(0, 0, -2), duration=.2, curve=curve.linear)
            self.player.arrow.shader = colored_lights_shader

        if self.level.bow.enabled and key == 'left mouse up':
            if mouse.hovered_entity and mouse.hovered_entity.visible:
                self.player.arrow.world_parent = scene
                self.player.arrow.animate('position', Vec3(*mouse.world_point), mouse.collision.distance / 500, curve=curve.linear, interrupt='kill')

                if mouse.hovered_entity == self.level.enemy:
                    invoke(self.destroyEnemy, delay=.3)
                    destroy(self.player.arrow, delay=.1)
                    return

                destroy(self.player.arrow, delay=10)

                if mouse.hovered_entity == self.level.enemy2:
                    invoke(self.destroyEnemy2, delay=.3)
                    destroy(self.player.arrow, delay=.1)
                    return

                destroy(self.player.arrow, delay=10)

                if mouse.hovered_entity == self.level.Cube:
                    invoke(self.openGate, delay=.3)
                    destroy(self.player.arrow, delay=.1)
                    return

                destroy(self.player.arrow, delay=10)

                #destroy arrows on enemy player
                if mouse.hovered_entity == self.enemyPlayer:
                    self.enemyPlayer.enabled = False
                    destroy(self.player.arrow, delay=.1)
                    self.startEnemyProgram = False
                    self.enemyPlayer.enabled = False
                    return

                destroy(self.player.arrow, delay=10)
                #destroy arrows on mob
                if mouse.hovered_entity == self.mob:
                    self.mob.enabled = False
                    destroy(self.player.arrow, delay=.1)
                    return

                destroy(self.player.arrow, delay=10)
            else:
                self.player.arrow.world_parent = scene
                self.player.arrow.animate('position', self.player.arrow.world_position + (self.player.arrow.forward * 100), .5, curve=curve.linear, interrupt='kill')
                destroy(self.player.arrow, delay=1)
        #cheats
        if key == 'z':
            self.level.bow.enabled = True
        if key == 'x':
            self.level.bow.enabled = False
        if key == 'c':
            invoke(self.createEnemy, delay=.3)
        if key == 'p':
            invoke(self.Anime)
        if key == 'g':
            invoke(self.openGate)
        if key == 'e':
            invoke(self.Enemy_Player)
        if key == 'm':
            invoke(self.load_mob_function)
        if key == "escape":
            sys.exit()
        if key == '-' or key == '- hold':
            self.damage(10)
        if key == '+' or key == '+ hold':
            self.heal(10)
        #animation controls
        #if key == 'w':
        #    self.player.moveForward()
            #for _ in self.player.moveForward():
            #        pass
        ##if key == 's':
        ##    self.player.moveBackward()
        #if key == 'a':
        #    #for _ in self.player.moveLeft():
        #    #    pass
        #    self.player.moveLeft()
        #if held_keys['ad'] :
        #    self.player.moveRight()

    def damage(self, value):
        self.HB1.value -= value
        self.player.health -= value

    def heal(self, value):
        self.HB1.value += value
        self.player.health += value

    def destroyEnemy(self):
        self.level.enemy.enabled = False

    def destroyEnemy2(self):
        self.level.enemy2.enabled = False
        self.textEnemy2.enabled = False
        self.textEnemy3.enabled = False

    def createEnemy(self):
        self.level.enemy2.enabled = True
        self.level.enemy2.collider = 'mesh'
        self.level.enemy2.color = color.blue

    def Anime(self):
        self.actor = Actor("assets/anime.glb")  # change filename to the GLB file
        self.actor.reparent_to(self.animeGirl)

        self.actor.play("moveForward")

    def turnOffChestLights(self):
        self.turnOffShader = True

    def update(self):
        #handle mob ai
        #self.mob.mob_movement(self.person, self.player.position)
        if self.player:
            self.mob.look_at(self.player)
            self.mob.rotation = Vec3(0,self.mob.rotation.y+180,0)
            self.enemyPlayer.look_at(self.player)
            self.enemyPlayer.rotation = Vec3(0,self.mob.rotation.y+180,0)
            self.animeGirl.look_at(self.player)
            self.animeGirl.rotation = Vec3(0,self.mob.rotation.y,0)

        original_chest_texture = self.level.chest.texture
        if not self.level.bow.enabled and mouse.hovered_entity in (self.level.chest, self.level.lid):
            if self.turnOffShader == False:
                self.level.chest.color = color.color(60, .4, .8)
                self.level.chest.shader = colored_lights_shader
                self.level.lid.color = color.color(60, .4, .8)
                self.level.lid.shader = colored_lights_shader
        else:
            self.level.chest.texture = original_chest_texture
            self.level.lid.texture = original_chest_texture
            self.level.chest.shader = None
            self.level.lid.shader = None

        if self.startEnemyProgram == True:
            if time.time() >= self.timer:
                #self.enemyPlayer.arrow = duplicate(self.level.arrow, world_parent=self.enemyPlayer, position=(0,2,0), rotation=Vec3(0, 0, 0))
                #self.enemyPlayer.arrow.shader = colored_lights_shader
                #self.enemyPlayer.arrow.world_parent = scene
                #self.enemyPlayer.arrow.animate('position', self.player.position,(self.player.position - self.enemyPlayer.position).length() / 1000,
                #                                curve=curve.linear, interrupt='kill')
                #if self.player.intersects(self.enemyPlayer):
                print(f"Enemy attacked player for {self.damage} damage!")
                self.player.health -= 10
                self.HB1.value -= 10#decrease the health bar
                    #self.enemyPlayer.arrow = duplicate(self.level.arrow,
                    #                                   world_parent=self.enemyPlayer,
                    #                                   position=Vec3(0, 3, 0),
                    #                                   rotation=Vec3(0, 0, 0))
                    #self.enemyPlayer.arrow.shader = colored_lights_shader
                    #self.enemyPlayer.arrow.world_parent = scene
                    #self.enemyPlayer.arrow.animate('position', Vec3(*mouse.world_point),
                    #                               mouse.collision.distance / 500,
                    #                            curve=curve.linear, interrupt='kill')
                    #self.enemyPlayer.bow = duplicate(self.level.bow, word_parent=self.enemyPlayer, position=self.enemyPlayer.position)
                self.enemyPlayer.arrow = duplicate(self.level.arrow, world_parent=self.enemyPlayer, position=(0,1,0), rotation=Vec3(0, 0, 0))
                self.enemyPlayer.arrow.shader = colored_lights_shader
                self.enemyPlayer.arrow.world_parent = scene
                self.enemyPlayer.arrow.animate('position', self.player.position,(self.player.position - self.enemyPlayer.position).length() / 50,
                                                curve=curve.linear, interrupt='kill')
                if self.target.health <= 0:
                    print("Game Over")
                    application.quit()

                else:
                    self.timer = time.time() + 3

            #if time.time() >= self.timer:


            #else:
            #    self.timer = time.time() + 3

        #if key == 'e':
        #    myMob.update()

    def openGate(self):
        self.level.gate1.animate_position(self.level.gate1.position+(self.level.gate1.left)*10,
                                duration=5,
                                curve=curve.linear)
        self.level.gate2.animate_position(self.level.gate2.position+(self.level.gate2.right)*10,
                                    duration=5,
                                    curve=curve.linear)

    def Enemy_Player(self):
        #self.target = self.player
        self.startEnemyProgram = True
        self.enemyPlayer.enabled = True
        #if self.target:
        self.enemyPlayer.add_script(SmoothFollow(target=self.target,
                                                offset = [0,3,0],
                                                #offset = [0,3,-10],
                                                speed =0.5)
                                )

    def load_mob_function(self):
        self.mob.enabled = True
        self.mob.action()
        #self.mob.follow()
        self.mob.add_script(SmoothFollow(target=self.target,
                                                #offset = [0,3,0],
                                                #offset = [0,3,-10],
                                                speed =0.5)
                                )

if __name__ == '__main__':
    app = Ursina()
    main_scene = MainScene()
    app.run()

