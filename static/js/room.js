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

function update_tile_image(name) {
    var result = document.getElementsByName(name);
	if (result.length > 0) {
		result[0].src = "/images/" + images[tiles[name]];
		result[0].title = images[tiles[name]].replace(".png", "").replace("_", " ");
	}
}

function set_tile_image(name, image) {
    var result = document.getElementsByName(name);
	if (result.length > 0) {
		result[0].src = "/images/" + images[image];
		result[0].title = images[image].replace(".png", "").replace("_", " ");
	}
}

function set_target(key, image) {
	target = key;
	document.getElementsByName('target_img')[0].src = '/images/' + images[image];
}

function set_action_href() {
	document.getElementsByName('action')[0].href = '/attack?target=' + target;
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
    if (exits[i] != -1) {
        set_tile_image(exit_xys[i], exit_images[i]);
        var result = document.getElementsByName(exit_xys[i] + "_exit");
	    if (result.length > 0) {
		    result[0].href = '/move?exit=' + i;
	    }
    }
}

for (i = 0; i < images.length; i++) {
	var result = document.getElementsByName("replace_" + i);
	for (j = 0; j < result.length; j++) {
		result[j].src = "/images/" + images[i];
	}
}

function keydown_handler(event) {
	var key_code = ('which' in event) ? event.which : event.keyCode;
	switch (key_code) {
	case 72:
	case 37:
	case 65:
		window.location = '/move?exit=0';
		return;
	case 74:
	case 40:
	case 83:
		window.location = '/move?exit=3';
		return;
	case 75:
	case 38:
	case 87:
		window.location = '/move?exit=2';
		return;
	case 76:
	case 39:
	case 68:
		window.location = '/move?exit=1';
		return;
	case 190:
		window.location = '/move?exit=4';
		return;
	}
}

window.onkeydown=keydown_handler;