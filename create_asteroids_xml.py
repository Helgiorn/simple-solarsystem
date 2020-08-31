# seed the pseudorandom number generator
import json
from random import seed
from random import *
# seed random number generator
seed(1)
# generate some random numbers

amount = 500
i = 0
sol = {}
sol['planets'] = []

while i <= amount:
    sol['planets'].append({
        'id': i + 100,
        'parentid': 1,
        'type': 3,
        'name': i,
        'angle': randint(0, 300),
        'display_radius': randint(45, 55),
        'radius': 300000.0,
        'size' : 2,
        'color' : [211, 211, 211],
    })
    i += 1

with open('asteroids.json', 'w') as outfile:
    json.dump(sol, outfile)