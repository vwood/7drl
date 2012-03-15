
#
# Tiles
#

images = ["floor1.png",
          "floor2.png",
          "floor3.png",
          "floor4.png",
          "floor5.png",
          "wall1.png",
          "wall2.png",
          "wall3.png",
          "wall4.png",
          "wall5.png",
          "door.png",
          "doorexit.png",
          "stairs.png",
          "water.png",
          "lava.png",
          "player.png",
          "catdog.png",
          "goblin.png",
          "dwarf.png",
          "janitor.png",
          "shopkeeper.png",
          "wizard.png",
          "bard.png",
          "cthulhu.png",
          "wand.png",
          "kobold_baby.png",
          "blank.png",
          "sword1.png",
          "sword2.png",
          "sword3.png"]

# Is a cell blocked by a tile?
blocked = [False, False, False, False, False,
           True, True, True, True, True,
           True, False, True, True, True,
           True, True, True, True, True,
           True, True, True, True, True, 
           True]

floors = [0, 1, 2, 3, 4]
walls = [5, 6, 7, 8, 9, 13, 14]
features = [10, 11, 12]
items = [24,27,28,29]
player = [15]
creatures = [16, 17, 18, 19, 20, 21, 22, 23, 25]
