#!/usr/bin/env python3
# coding: utf8
import string
VERSION = '1.3.1'
class Window:
    @property
    def Size(self): return (256, 256)
class Image:
    @property
    def Quantity(self): return 3
    @property
    def Size(self): return (256, 256)
class Color:
    @property
    def Quantity(self): return 16
class Tile:
    @property
    def Quantity(self): return 1024
    @property
    def Size(self): return (8, 8)
class Map:
    @property
    def Quantity(self): return 8
    @property
    def Size(self): return (256, 256)
class Sound:
    @property
    def Quantity(self): return 64
class Music:
    @property
    def Quantity(self): return 8
    @property
    def HasChannelQuantity(self): return 4
class Channel:
    @property
    def HasSoundQuantity(self): return 32

Window = Window()
Image = Image()
Color = Color()
Tile = Tile()
Map = Map()
Sound = Sound()
Music = Music()
Channel = Channel()

