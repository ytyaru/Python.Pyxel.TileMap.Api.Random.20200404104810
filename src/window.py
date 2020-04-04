#!/usr/bin/env python3
# coding: utf8
import pyxel, numpy, itertools, PyxelSpec
class App:
    def __init__(self):
        self.window = Window()
        pyxel.init(self.window.Width, self.window.Height, border_width=0, caption=self.window.Caption)
        self.map = Map()
        pyxel.run(self.update, self.draw)
    def update(self):
        self.map.update()
    def draw(self):
        pyxel.cls(0)
        self.map.draw()
        pyxel.text(0, 0, 'Press the SPACE key.\nMaps are randomly generated.', 7)
class Window:
    @property
    def Width(self): return 128
    @property
    def Height(self): return 96
    @property
    def Caption(self): return "TileMap API"
class TileImage:
    def __init__(self):
        self.__set_image0()
    def __set_image0(self):
        pyxel.image(self.Id).set(0, 0, [
            "3333333333333333",
            "333333333333a333",
            "33333b33333a7a33",
            "33333b333333a333",
            "33333b333333b333",
            "3b333333333bbb33",
            "3b3333333333b333",
            "3333333333333333",
            "4444444400000000",
            "4444444400000000",
            "44444d4400000000",
            "4444444400000000",
            "4444444400000000",
            "4444444400000000",
            "4d44444400000000",
            "4444444400000000",
        ])
    @property
    def Id(self): return 0
    @property
    def StartId(self): return 0
    @property
    def EndId(self): return 1
    @property
    def Width(self): return pyxel.tilemap(self.Id).width
    @property
    def Height(self): return pyxel.tilemap(self.Id).height
class Map:
    def __init__(self):
        self.__tile = TileImage()
        self.__id = 0
        self.generate()
    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE): self.generate()
    def draw(self):
        pyxel.bltm(0, 0, self.Id, 0, 0, self.Tile.Width, self.Tile.Height)
    @property
    def Tile(self): return self.__tile
    @property
    def Id(self): return self.__id
    def generate(self):
        self.__generate_random_map()
        self.__format_num_to_str()
        pyxel.tilemap(self.Id).refimg = self.Tile.Id
        pyxel.tilemap(self.Id).set(0, 0, self.__to_tile_id_lists())
    def __generate_random_map(self):
        numpy.set_printoptions(formatter={"int": "{:03x}".format})
        self.__data = \
            numpy.random.randint(
                self.Tile.StartId, self.Tile.EndId + 1,
                (PyxelSpec.Map.Size[0], PyxelSpec.Map.Size[1])
            ).reshape(
                PyxelSpec.Map.Size[0], PyxelSpec.Map.Size[1])
        self.__data = self.__data.tolist()
    def __format_num_to_str(self):
        for x in range(PyxelSpec.Map.Size[0]):
            for y in range(PyxelSpec.Map.Size[1]):
                self.__data[x][y] = format(self.__data[x][y], '03x')
    def __to_tile_id_lists(self):
        res = []
        for y in range(len(self.__data)):
            res.append(''.join(self.__data[y]))
        return res

App()
