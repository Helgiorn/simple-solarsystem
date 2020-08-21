import math

class PlanetaryObject:

    def __init__(self, id):
        self.id = id
        self.parentid = 0
        self.name = ""
        self.color = ""
        self.radius = 0
        self.display_radius = 0
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
        self.TIME_FACTOR = 1000000
        self.GRAVITATIONAL_CONSTANT = 6.7 * math.pow(10, -11)

        #init the rest (find a better way?)
        
        self.read_object()
        # self.read_parent()
        # #hack, not all mass calculations are ok with 10, 24
        # self.mass = float(self.mass) * math.pow(10, 24)
        # self.radius = float(self.radius) * math.pow(10, 11)
        # self.calculate_simulation_period()
        # self.angle_per_frame()
        # self.x = (round((self.display_radius * math.cos(self.angle)) + self.parent_x, 2))
        # self.y = (round((self.display_radius * math.sin(self.angle)) + self.parent_y, 2))
    
    def read_object(self):
        with open('planets.txt', encoding="utf8") as f:
            
            for line in f:
                parts = line.split(",")
                if str(self.id) == parts[0]:
                    self.id = parts[0]
                    self.parentid = parts[1]
                    self.type = parts[2]
                    self.name = parts[3]
                    self.color = parts[4]
                    self.radius = float(parts[5])
                    self.display_radius= float(parts[6])
                    self.angle = float(parts[7])
                    #TODO: this is a hack, mass needs better handling later.
                    self.mass = parts[8]

    #get parent mass
    def read_parent(self):
        with open('planets.txt', encoding="utf8") as f:
            for line in f:
                parts = line.split(",")
                if str(self.parentid) == parts[0]:
                    self.parent_name = parts[3]
                    self.parent_mass = int(parts[8]) * math.pow(10, 30)
                    self.parent_angle = float(parts[7])
                    self.parent_display_radius = float(parts[6])

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


solarsystem = []

with open('planets.txt', encoding="utf8") as f:
    for line in f:
        parts = line.split(",")
        solarsystem.append(PlanetaryObject(parts[0]))

for object in solarsystem:
    print (object.name)