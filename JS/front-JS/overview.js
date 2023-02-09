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

let singapore_marker = L.marker([1.3521, 103.8198]).addTo(map);

let golden_gate = L.circle([1.4, 103.8198], {
    color: "red",
    fillColor: "#f03",
    fillOpacity: "0.5",
    radius: 1500
}).addTo(myMap);


