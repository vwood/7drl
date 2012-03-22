var images = ["Rock_Floor.png",
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
			  "Tree.png"];

for (i = 0; i < images.length; i++) {
	var result = document.getElementsByName("replace_" + i);
	for (j = 0; j < result.length; j++) {
		result[j].src = "/images/" + images[i];
	}
}
