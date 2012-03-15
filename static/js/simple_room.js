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
              "kobold_baby.png"];

function update_tile_image(name) {
    var result = document.getElementsByName(name);
	if (result.length > 0) {
		result[0].src = "/images/" + images[tiles[name]];
	}
}

function set_tile_image(name, image) {
    var result = document.getElementsByName(name);
	if (result.length > 0) {
		result[0].src = "/images/" + images[image];
	}
}

// Not used - was fun playing around with a map editor
function on_image_click(name) {
    tiles[name]++;
    if (tiles[name] >= images.length) {
        tiles[name] = 0;
    }
    update_tile_image(name);
}


for (i = 0; i < tiles.length; i++) {
    update_tile_image(i);
}

for (i = 0; i < items.length; i++) {
    set_tile_image(free_space[i], items[i]);
}

var height = tiles.length / width;

function xy_to_index(x, y) {
	return Math.floor(x + y * width);
}

var mid_x = Math.floor(width / 2);
var mid_y = Math.floor(height / 2);

var exit_xys = [xy_to_index(0, mid_y),
				xy_to_index(width - 1, mid_y),
				xy_to_index(mid_x, 0),
				xy_to_index(mid_x, height - 1),
				xy_to_index(mid_x, mid_y)];


var exit_images = [11, 11, 11, 11, 12];

for (i = 0; i < exits.length; i++) {
    if (exits[i] != "None") {
        set_tile_image(exit_xys[i], exit_images[i]);
        var result = document.getElementsByName(exit_xys[i] + "_exit");
	    if (result.length > 0) {
		    result[0].href = exits[i];
	    }
    }
}

for (i = 0; i < images.length; i++) {
	var result = document.getElementsByName("replace_" + i);
	for (j = 0; j < result.length; j++) {
		result[j].src = "/images/" + images[i];
	}
}