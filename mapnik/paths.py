import os

mapniklibpath = '/usr/lib/mapnik'
mapniklibpath = os.path.normpath(mapniklibpath)
inputpluginspath = '/usr/lib/mapnik/3.0/input'
fontscollectionpath = '/usr/share/fonts'
__all__ = [mapniklibpath,inputpluginspath,fontscollectionpath]
