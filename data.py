from ursina import *

ground = ()
player_model = "assets/Jinx.gltf"
player_action_running = "JinxRigAction.1"
player_actions_combo = ("JinxRigAction.1","JinxRigAction.1","JinxRigAction.1")
last_move_button = (0,0) # [0]key [1]time
last_attack_button = (0,0,0) # [0]key [1]time [2]combo len

class Character():
    def __init__(self):
        self.str = 6
        self.agi = 1
        self.vit = 1
        self.luk = 5
        #self.speed = 4
        self.speed = 40#added on 5/24/23
        self.health = 60
        self.scale = 10#added on 5/24/23
        self.invulnerable = False
