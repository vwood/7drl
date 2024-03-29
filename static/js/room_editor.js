Array.prototype.map = function(fn) {
    var result = [];
    var length = this.length;
    for (i = 0; i < length; i++) {
        result.push(fn(this[i]));
    }
    return result;
};

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

var tiles = [[1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1]];

function update_tile_image(x, y) {
    document.getElementsByName(x+"_"+y)[0].src = images[tiles[x][y]];
}

function update_tile_value() {
    tile_string = tiles.join(",");
    document.getElementsByName(tiles[0].value = );
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