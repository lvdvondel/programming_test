# imports

import pygame
import random

class World_Map():
    """ This class is used to create a World Map"""
    world_map_exists = False

    def __init__(self, xlim, ylim, zlim = 0):
        self.xlim = xlim
        self.ylim = ylim
        self.zlim = zlim
        World_Map.world_map_exists = True 

    def __str__(self):
        rep = "World Map:"
        return rep

class Tile():
    """Creates tiles to fill the world map"""

    #Constructor
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        rep = "This is a tile with location [x, y, z]:" + "[" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "]"
        return(rep)
    
class Living_Object():
    """This class is a parent for npcs and playable characters"""
    
    #constructor
    def __init__(self, image, x, y, z):
        self.image = image
        self.x = x
        self.y = y
        self.z = z

    #print object info
    def __str__(self):
        rep = "This is an object that can move. The current location [x, y, z] is:"
        rep = rep + "[" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "]"
        return rep
    
    def get_coordinates(self):
        Coord_lib = {"x": self.x, "y": self.y, "z": self.z}
        return(Coord_lib)

class Player_character(Living_Object):
    """This class inherits from Living_Object and is controlled by the player"""
    
    #constructor
    def __init__(self, x, y, z, name, image):
        super().__init__(x, y, z)
        self.name = name

class NPC(Living_Object):
    """This class inherits from Living_Object and is computer controlled"""
    
    #count number of active NPC's to avoid overpopulation
    count_NPC = 0
    
    #Constructor: 
    def __init__(self, x, y, z, name):
        super().__init__(x, y, z)
        self.name = name
        NPC.count_NPC +=1 #increase count of NPC's by 1 when a new NPC is constructed

#main


