// Creating map options
var mapOptions = {
    center: [1.3521, 103.8198],
    zoom: 12
}

// Creating a map object
var map = new L.map('map', mapOptions);
// Creating a Layer object
var layer = new L.TileLayer('http://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png');
// Adding layer to the map
map.addLayer(layer);


