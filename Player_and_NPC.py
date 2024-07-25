# imports

class Living_Object():
    """This class is a parent for npcs and playable characters"""
    
    #constructor
    def __init__(self, x, y, z):
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
    def __init__(self, x, y, z, name):
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
        count_NPC +=1 #increase count of NPC's by 1 when a new NPC is constructed

#main

Bernard = Player_character(0,0,0, 'Bernard')
print(Bernard.get_coordinates())
