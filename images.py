#
# Tiles
#

images = ["Rock_Floor.png",
          "Stone_Floor.png",
          "Dirt_Floor.png",
          "Red_Floor.png",
          "Moss_Floor.png",
          "Rock_Wall.png",
          "Stone_Wall.png",
          "Dirt_Wall.png",
          "Red_Wall.png",
          "Mossy_Wall.png",
          "Door.png",
          "Open_Door.png",
          "Stairs.png",
          "Water.png",
          "Lava.png",
          "Rogue.png",
          "Cat-dog.png",
          "Goblin.png",
          "Dwarf.png",
          "Janitor.png",
          "Shopkeeper.png",
          "Wizard.png",
          "Bard.png",
          "Cthulhu.png",
          "Wand.png",
          "Kobold_Baby.png",
          "Blank.png",
          "Gold_Sword.png",
          "Crystal_Sword.png",
          "Silver_Sword.png",
          "Spaniard.png",
          "Hat_Guy.png",
          "Tree.png"]

# Is a cell blocked by a tile?
blocked = [False, False, False, False, False, # 0 - 4
           True, True, True, True, True, # 5 - 9
           True, False, True, True, True, # 10 - 14
           True, True, True, True, True, # 15 - 19
           True, True, True, True, True, # 20 - 24
           True, True, True, True, True, # 25 - 29
           True, True, True, True] # 30 - 33

# blank = 26
floors = [0, 1, 2, 3, 4]
walls = [5, 6, 7, 8, 9, 13, 14, 32]
features = [10, 11, 12]
items = [24,27,28,29]
player = [15, 30, 31]
creatures = [16, 17, 18, 19, 20, 21, 22, 23, 25]

wall_names = [["Rocky ", "Cold ", "Rock ", "Jagged "],
              ["Deep ", "Stoney ", "Stone ", "Cyclopean "],
              ["Underground ", "Earthen ", "Clay "],
              ["Bloody ", "Violent ", "Stained ", "Elegiac "],
              ["Slimy ", "Moist ", "Slippery ", "Noisome "],
              ["Island ", "Moist ", "Wet ", "Antediluvian "],
              ["Hellish ", "Blasted ", "Volcanic ", "Unholy "],
              ["Forest ", "Druidic ", "Overgrown ", "Fertile"]]

floor_names = [["Cavern", "Lair"],
               ["Room", "Temple", "Crypt"],
               ["Burrow", "Soil", "Hole"],
               ["Pit", "Temple", "Lair"],
               ["Grove", "Growth", "Algae"]]

monster_health = [40, 30, 50, 80, 90, 120, 60, 400, 10]
