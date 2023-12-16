// main.js

var map = L.map('map').setView([0, 0], 2);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

console.log("pothole_data:", pothole_data);

pothole_data.forEach(function (pothole) {
    var marker = L.marker([pothole.latitude, pothole.longitude]).addTo(map);

    var popupContent = '<img src="' + pothole.image_path + '" alt="Pothole Image" style="max-width: 100%;">';
    marker.bindPopup(popupContent);
});
