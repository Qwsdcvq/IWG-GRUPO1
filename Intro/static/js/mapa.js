var map = L.map('map').fitWorld();

var osm = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap'
}).addTo(map);

googleStreets = L.tileLayer('http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',{
    maxZoom: 20,
    subdomains:['mt0','mt1','mt2','mt3']
 });

var CyclOSM = L.tileLayer('https://{s}.tile-cyclosm.openstreetmap.fr/cyclosm/{z}/{x}/{y}.png', {
	maxZoom: 20,
	attribution: '<a href="https://github.com/cyclosm/cyclosm-cartocss-style/releases" title="CyclOSM - Open Bicycle render">CyclOSM</a> | Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
});
osm.addTo(map);


var AutosElec = L.layerGroup([
    L.marker([-33.4090837634595, -70.54501695537513]),
    L.marker([-33.34485915510649, -70.5436875031083]),
    L.marker([-33.68157094638871, -70.7263926204931]),
    L.marker([-33.685645269393525, -70.72605326845714]),
    L.marker([-33.57970763081137, -70.71372668583395]),
    L.marker([-33.44027677339363, -70.84138125960195]),
    L.marker([-33.423856188361704, -70.57959995053842]),
    L.marker([-33.40548366859819, -70.59836526018697]),
    L.marker([-33.41326323172434, -70.67890871774689])
]);

var Lime = L.polygon([
    [-33.41624070572781, -70.60830078293743],
    [-33.38973278096419, -70.60210996713857],
    [-33.36949907171547, -70.58247243274548],
    [-33.36088164013337, -70.49686609604055],
    [-33.39327663687089, -70.49858708998791],
    [-33.41175913185684, -70.50556012937608],
    [-33.4291465498631, -70.53903071755468],
    [-33.43278364463819, -70.58470412483322],
    [-33.41634276414807, -70.60910976192665],
],{color: 'green'})

var BikeItau = L.layerGroup([
    L.marker([-33.45754380881102, -70.66399799473814]).bindPopup("S57 - Beauchef, Santiago, Región Metropolitana"),
    L.marker([-33.45676252045868, -70.66007429093196]).bindPopup("S54 - Plaza Ercilla, Santiago, Región Metropolitana"),
    L.marker([-33.45429167546263, -70.6629095241156]).bindPopup("S35 - José Miguel Carrera, 8370272 Santiago, Región Metropolitana"),
    L.marker([-33.45354956555316, -70.66721530894793]).bindPopup("S64 - República / Gorbea, 8370267 Santiago, Región Metropolitana"),
    L.marker([-33.45155499604872, -70.6656414552738]).bindPopup("S044 - Plaza Manuel Rodríguez, 8370135 Santiago, Región Metropolitana"),
    L.marker([-33.44921655139074, -70.67253922758778]).bindPopup("S46 - Metro ULA, 8350667 Santiago, Región Metropolitana"),
    L.marker([-33.448682194399176, -70.66817588128704]).bindPopup("S02 - Metro República, 8370039 Santiago, Región Metropolitana"),
    L.marker([-33.445223561635075, -70.66804076900317]).bindPopup("S40 - Erasmo Escala, Santiago, Región Metropolitana"),
    L.marker([-33.451737759323294, -70.65961809429828]).bindPopup("S32 - Gorbea, Santiago, Región Metropolitana"),
    L.marker([-33.44769155239204, -70.66129593628756]).bindPopup("S07 - Metro Los Héroes, 8370007 Santiago, Región Metropolitana"),
    L.marker([-33.438124101125666, -70.65915753661494]).bindPopup("S18 - Metro Santa Ana, 8340309 Santiago, Región Metropolitana"),
    L.marker([-33.44174729116835, -70.65940530337151]).bindPopup("S01 - Agustinas / Manuel Rodríguez Norte, 8340473 Santiago, Región Metropolitana"),
    L.marker([-33.445388542751836, -70.65930754113404]).bindPopup("S41 - Fanor Velasco, 8340531 Santiago, Región Metropolitana"),
    L.marker([-33.45278583331308, -70.65765701514181]).bindPopup("S11 - Metro Toesca, 8331159 Santiago, Región Metropolitana"),
    L.marker([-33.43978715644518, -70.65516017289642]).bindPopup("S27 - Teatinos / Huérfanos, Santiago, Región Metropolitana"),
    L.marker([-33.44226933091695, -70.65479164340225]).bindPopup("S19 - Palacio de La Moneda, Santiago, Región Metropolitana"),
    L.marker([-33.44890674198343, -70.65328267059394]).bindPopup("S80 - Nataniel cox / Miguel Olivares, 8330349 Santiago, Región Metropolitana"),
    L.marker([-33.4513316218528, -70.65060314479207]).bindPopup("S39 - Metro Parque Almagro, 8330530 Santiago, Región Metropolitana"),
    L.marker([-33.447229016153294, -70.64883973801857]).bindPopup("S15 - Serrano / Tarapacá, Santiago, Región Metropolitana"),
    L.marker([-33.45704466162762, -70.66907049566761]).bindPopup("S58 - Domeyko / Av. España, Santiago, Región Metropolitana"),
    L.marker([-33.44998971412174, -70.64663536860685]).bindPopup("S56 - Condor, Santiago, Región Metropolitana"),
    L.marker([-33.45018146468332, -70.64305792582725]).bindPopup("S17 - San Isidro / Santa Isabel, Región Metropolitana"),
    L.marker([-33.449714419451226, -70.6361750877663]).bindPopup("S31- Raulí, 8330373 Santiago, Región Metropolitana"),
    L.marker([-33.44522792452533, -70.63677650928726]).bindPopup("S50 - Gral. Jofré, 8330162 Santiago, Región Metropolitana"),
    L.marker([-33.44161763788633, -70.63841119173924]).bindPopup("S37 - FAU, Santiago, Región Metropolitana"),
    L.marker([-33.44029488365702, -70.64708273946076]).bindPopup("S16 - Teatro Municipal, 8320191 Santiago, Región Metropolitana"),
    L.marker([-33.44889205051947, -70.63219558377003]).bindPopup("S52 - Argomedo, 8330397 Santiago, Región Metropolitana"),
    L.marker([-33.44531553106889, -70.61198563255084]).bindPopup("P07 - Eduardo de La Barra, 7501398 Santiago, Región Metropolitana"),
    L.marker([-33.43513590382594, -70.6087063844559]).bindPopup("P59 - Los Estanques, 7500731 Santiago, Región Metropolitana"),
    L.marker([-33.446838659031805, -70.60204493148645]).bindPopup("Hernán Cortés 2743, 7770080 2791, Ñuñoa, Región Metropolitana"),
    L.marker([-33.428375831177, -70.59484289236936]).bindPopup("P22 - Plaza Loreto Cousiño, Providencia, Santiago, Región Metropolitana"),
    L.marker([-33.426172868540284, -70.59060879388414]).bindPopup("LC017 - Sánchez Fontecilla / Cristóbal Colón, Las Condes, Región Metropolitana")
]);

L.control.layers({
    "OpenStreetMap": osm,
    "Google Map": googleStreets,
    "Ciclovias": CyclOSM
},{
    "Puntos Electricos": AutosElec,
    "Lime": Lime,
    "Bicicletas Itau": BikeItau
}).addTo(map);

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