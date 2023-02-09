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

let sfo_marker = L.marker([0.31430, 103.79117]).addTo(map);
let oak_marker = L.marker([37.710, -122.224]).addTo(map);
let sjc_marker = L.marker([37.361, -121.928]).addTo(map);


