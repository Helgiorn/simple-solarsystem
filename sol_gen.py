import math
import csv

class PlanetaryObject:

    def __init__(self, id):
        self.id = id
        self.name = ""
        self.angle = 0.1
        self.display_radius = 0.1
        self.radius = 0.1 
        self.period = 0.1
        self.angle_per_frame = 0.1
        self.x = 0.01
        self.y = 0.01
        self.read_values()
    
    def read_values(self):
        with open('planets.txt', encoding="utf8") as f:
            
            #ID,ParentID,type,Name,Radius,OrbitalRadius,Angle,Mass
            for line in f:
                parts = line.split(",")
                if str(self.id) == parts[0]:
                    self.id = parts[0]
                    self.name = parts[1]
                    self.angle = parts[2]
                    self.display_radius = float(parts[3])
                    self.radius = float(parts[4]) * math.pow(10, 11)
    
    def update_period(self, period):
        self.period = float(period)
    
    def update_angle(self, angle):
        self.angle = angle
    
    def update_x(self, x):
        self.x = x

    def update_y(self, y):
        self.y = y
        
    def update_angle_tick(self):
        self.angle = float(self.angle) + float(self.angle_per_frame)