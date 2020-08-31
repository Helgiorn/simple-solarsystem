import math
import json

class PlanetaryObject:

    def __init__(self, id):
        self.id = id
        self.parentid = 0
        self.type = 0
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
        self.size = 0
        self.color = ""

        self.read_from_json()

    def read_from_json(self):
        data = {}
        with open('planets.json') as json_file:
            planets = json.load(json_file)
            for p in planets['planets']:
                if p['id'] == self.id:
                    self.parentid = p['parentid']
                    self.type = p['type']
                    #self.id = p['id']
                    self.name = p['name']
                    self.angle = p['angle']
                    self.display_radius = p['display_radius'] + 25
                    self.radius = p['radius']
                    self.size = p['size']
                    self.color = p['color']
  

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
        self.angle = float(self.angle) + float(self.angle_tick)