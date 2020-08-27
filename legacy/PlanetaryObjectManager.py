import math
import csv

class PlanetaryObject:

    def __init__(self, id):
        self.id = id
        self.type = 0
        self.parentid = 0
        self.name = ""
        self.color = ""
        self.radius = 0
        self.orbital_radius = 0
        self.angle = 0
        self.mass = 0
        self.period = 0
        self.radians_per_frame = 0
        self.parent_mass = 0
        self.parent_name = 0
        self.x = 0
        self.y = 0
        self.parent_x = 0
        self.parent_y = 0
     
        #these need inheritance, static in class for now, need to be changed in two places to be correct
        self.FRAMES_PER_SECOND = 60
        self.TIME_FACTOR = 10000
        self.GRAVITATIONAL_CONSTANT = 6.7 * math.pow(10, -11)

        #init the rest (find a better way?)
        
        self.read_object()
        #self.read_parent()
        #hack, not all mass calculations are ok with 10, 24
        self.mass = float(self.mass) * math.pow(10, 24)
        self.radius = float(self.radius) * math.pow(10, 11)
        self.calculate_simulation_period()
        self.angle_per_frame()
        self.x = (round((self.orbital_radius * math.cos(self.angle)) + self.parent_x, 2))
        self.y = (round((self.orbital_radius * math.sin(self.angle)) + self.parent_y, 2))
    
    def read_object(self):
        with open('planets.txt', encoding="utf8") as f:
            
            #ID,ParentID,type,Name,Radius,OrbitalRadius,Angle,Mass
            for line in f:
                parts = line.split(",")
                if str(self.id) == parts[0]:
                    self.id = parts[0]
                    self.parentid = parts[1]
                    self.type = parts[2]
                    self.name = parts[3]
                    self.radius = float(parts[4])
                    self.orbital_radius= float(parts[5])
                    self.angle = float(parts[6])
                    self.mass = parts[7]

    # #TODO: get parent mass
    # def read_parent(self):
    #     parent = PlanetaryObject(self.parentid)
    #     self.parent_name = parent.name()
    #     self.parent_x = parent.parent_x
    #     self.parent_y = parent.parent_y

    def write_object():
        pass
    
    def calculate_simulation_period(self):
        self.period = (2 * math.pi * math.pow(float(self.radius), 3 / 2)) / math.pow(self.GRAVITATIONAL_CONSTANT * self.parent_mass, 1 / 2)
        accelerated_period = self.period / self.TIME_FACTOR
        self.period = round(accelerated_period, 2)

    def angle_per_frame(self):
        total_frames = self.period * self.FRAMES_PER_SECOND
        # Multiply by minus one so we orbit counter-clockwise
        self.radians_per_frame = -1 * (2 * math.pi) / total_frames

earth = PlanetaryObject(4)
print (earth.parent_name)