var images = ["floor1.png",
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
              "opendoor.png",
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
              "wand.png"];

function update_tile_image(x, y) {
	var name = x + "_" + y;
    var result = document.getElementsByName(name);
	if (result.length > 0) {
		result[0].src = "/images/" + images[tiles[x][y]];
	}
}

function on_image_click(name) {
    var coords = name.split("_");
    var x = coords[0];
    var y = coords[1];

    tiles[x][y]++;
    if (tiles[x][y] >= images.length) {
        tiles[x][y] = 0;
    }

    update_tile_image(x, y);
}


for (i = 0; i < tiles.length; i++) {
    for (j = 0; j < tiles[i].length; j++) {
        update_tile_image(i, j);
    }
}
