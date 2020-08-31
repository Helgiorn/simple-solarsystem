import math
import csv

class PlanetaryObject:

    def __init__(self, id):
        self.id = id
        self.name = ""
        self.angle = 0.1
        self.new_angle = 0.0
        self.display_radius = 0.1
        self.radius = 0.1 
        self.period = 0.1
        self.angle_tick = 0.1
        self.x = 0.01
        self.y = 0.01
        self.au = 1.496e+8 * 2


        self.read_values()
    
    def read_values(self):
        with open('planets.txt', encoding="utf8") as f:
            
            #ID,name,angle,display_radius,radius
            for line in f:
                parts = line.split(",")
                if str(self.id) == parts[0]:
                    self.id = parts[0]
                    self.name = parts[1]
                    self.angle = parts[2]
                    self.display_radius = float(parts[3])
                    self.radius = float(parts[4])

    def update_period(self, period):
        self.period = float(period)
    

    def update_angle(self, angle):
        self.angle = float(angle)
    

    def update_x(self, x):
        self.x = x


    def update_y(self, y):
        self.y = y
    
    def update_angle_per_frame(self, angle_tick):
            self.angle_tick = float(angle_tick)

    def update_tick(self):
        #print(self.name, self.angle, self.angle_tick)
        self.angle = float(self.angle) + float(self.angle_tick)
        #print(self.name, self.angle)

