from bearlibterminal import terminal
from enum import Enum
import maptools
from maptools import Tile
from maptools import Terrain

# map = maptools.create_worldmap(80, 25)
# terminal.set("font: Nobbins.png, size=9x12, codepage=437")


class Cursor:
    def __init__(self, x, y, menuitems):
        self.x = x
        self.y = y
        self.symbol = ord(">")
        self.start = y
        self.end = y + menuitems

    def clear(self):
        terminal.put(self.x, self.y, ord(' '))

    def move(self, dy):
        if self.y + dy >= self.start and self.y + dy <= self.end:
            self.clear()
            self.y += dy
            terminal.color('white')
            terminal.put(self.x, self.y, self.symbol)


class Sidebar:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tiles = [Tile(t) for t in Terrain]
        self.cursor = Cursor(x-1, y, len(self.tiles)-1)
        self.selected = self.tiles[1]
        self.render_cursor()

        for i, tile in enumerate(self.tiles):
            terminal.color('white')
            terminal.printf(x+2, y+i, tile.name)
            terminal.color(tile.color)
            terminal.put(x, y+i, tile.symbol)

    def render_cursor(self):
        terminal.color('white')
        terminal.put(self.cursor.x, self.cursor.y, self.cursor.symbol)


def render_map(map_a):
    for yArray in map_a:
        for xArray in yArray:
            terminal.color(terminal.color_from_name(str(xArray.ttype)))
            terminal.put(xArray.x+25, xArray.y+5, 64)


def print_charset(point):
    terminal.printf(10, 10, "test")
    height = int(terminal_size[1])
    width = int(terminal_size[0])
    for y in range(0, height):
        for x in range(0, width):
            terminal.put(x, y, point)
            point += 1

# def render_sidebar(x, y):


def handle_keys():
    key = terminal.read()
    global mouse_pressed
    if key == terminal.TK_DOWN:
        sidebar.cursor.move(1)
    if key == terminal.TK_UP:
        sidebar.cursor.move(-1)
    if key == terminal.TK_MOUSE_SCROLL:
        sidebar.cursor.move(terminal.state(terminal.TK_MOUSE_WHEEL))
    if key & terminal.TK_KEY_RELEASED == terminal.TK_KEY_RELEASED:
        terminal.layer(1)
        terminal.put(terminal.state(terminal.TK_MOUSE_X), terminal.state(
            terminal.TK_MOUSE_Y), sidebar.selected.symbol)
        terminal.layer(0)
        mouse_pressed = False
        for coord in mouse_map:
            terminal.layer(0)
            terminal.bkcolor('black')
            terminal.put(coord[0], coord[1], sidebar.selected.symbol)
        mouse_map.clear()
    if key == terminal.TK_MOUSE_LEFT:
        mouse_pressed = True
    if key == terminal.TK_MOUSE_MOVE:
        terminal.layer(2)
        terminal.put(terminal.state(terminal.TK_MOUSE_X), terminal.state(
            terminal.TK_MOUSE_Y), sidebar.selected.symbol)
        terminal.layer(0)
        if mouse_pressed is True:
            mouse_x = terminal.state(terminal.TK_MOUSE_X)
            mouse_y = terminal.state(terminal.TK_MOUSE_Y)
            terminal.layer(0)
            terminal.bkcolor('grey')
            terminal.put(mouse_x, mouse_y, ord(' '))
            mouse_map.append((mouse_x, mouse_y))

    if key == terminal.TK_F1:
        print_charset(1000)
    if key == terminal.TK_ESCAPE:
        return 0


# def move_cursor(x, y):


terminal.open()

# Width x Height
terminal_size = list(map(int, terminal.get("window.size").split("x")))
terminal.printf(0, 0, "Width: " + str(terminal_size[0]))
terminal.printf(0, 1, "Height: " + str(terminal_size[1]))

sidebar = Sidebar(2, 8)

#Input Variables
mouse_pressed = False
mouse_map = []



terminal.refresh()


while (handle_keys() != 0):
    terminal.refresh()
    terminal.layer(2)
    terminal.clear_area(0, 0, terminal_size[0], terminal_size[1])
    terminal.layer(0)


terminal.close()
