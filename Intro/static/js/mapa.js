
var map = L.map('map').fitWorld();

var osm = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap'
}).addTo(map);

var osmH = L.tileLayer('https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'

})

L.control.layers({
    "OpenStreetMap": osm,
    "OpenStreetMap.HOT": osmH
}).addTo(map);
osm.addTo(map);


map.locate({setView: true, maxZoom: 16});

function onLocationFound(e) {
    var radius = e.accuracy;

    L.marker(e.latlng).addTo(map)
        .bindPopup("Estas a " + Math.trunc(radius) + " metros de este punto").openPopup();

    L.circle(e.latlng, radius).addTo(map);
}

map.on('locationfound', onLocationFound);

function onLocationError(e) {
    alert(e.message);
}

map.on('locationerror', onLocationError);


