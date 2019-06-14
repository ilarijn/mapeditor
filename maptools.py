import random
from aenum import Enum, NoAlias
from bearlibterminal import terminal


class Terrain(Enum):

    _settings_ = NoAlias

    grass = {
        'symbol': ord('.'),
        'name': 'Grass'
    }
    forest = {
        'symbol': 9572,
        'name': 'Forest'
    }
    hill = {
        'symbol': ord('n'),
        'name': 'Hill'
    }
    mountain = {
        'symbol': ord('^'),
        'name': 'Mountain'
    }
    water_shallow = {
        'symbol': ord('~'),
        'name': 'Water (shallow)'
    }
    water_deep = {
        'symbol': ord('~'),
        'name': 'Water (deep)'
    }

    def __str__(self):
        return self.name


class Tile:

    def __init__(self, terrain_type):
        self.ttype = terrain_type
        self.name = terrain_type.value.get('name')
        self.color = terminal.color_from_name(terrain_type.name)
        self.symbol = terrain_type.value.get('symbol')

    def __iter__(self):
        return self

    def clear(self):
        terminal.put(self.x, self.y, ord(' '))


def create_worldmap(width, height):
    map = [[Tile(x, y, Terrain.types().get(random.randint(0, 5)))
            for y in range(height)]
           for x in range(width)]

    return map
