# imports

class Player(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_coordinates(self):
        print("x = " +  str(self.x) + "y = "+ str(self.y) + "z = " + str(self.z))
        coord = {"x":self.x, "y":self.y, "z":self.z}
        return(coord)

class Generic_npc(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_coordinates(self):
        print("x = " +  str(self.x) + "y = "+ str(self.y) + "z = " + str(self.z))
        coord = {"x":self.x, "y":self.y, "z":self.z}
        return(coord)
    
#main