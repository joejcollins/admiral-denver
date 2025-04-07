---
layout: default
title: Survey Location
parent: Survey
---

Survey area.

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css"
   integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
   crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.6.0/dist/leaflet.js"
   integrity="sha512-gZwIG9x3wUXg2hdXF6+rVkLF/0Vi9U8D2Ntg4Ga5I5BZpVkVxlJWbSQtXPSiUTtC0TjtGOmxa1AJPuV0CPthew=="
   crossorigin=""></script>
<script src='//api.tiles.mapbox.com/mapbox.js/plugins/leaflet-omnivore/v0.3.1/leaflet-omnivore.min.js'></script>


<div id="map" style="height:525px; width:525px;"></div>
<script>
    var map = L.map('map', {
        center: [51.970927,0.4396255],
        zoom: 13
    });
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 16,
        id: 'mapbox/streets-v11',
        accessToken: 'pk.eyJ1Ijoiam9lamNvbGxpbnMiLCJhIjoiY2s1djkydG04MGF0aDNtbWRoeWV5azZrMyJ9.4q2Mqrow-1aCB5bXkJEDDA'
    }).addTo(map);
    var runLayer = omnivore.gpx('https://raw.githubusercontent.com/joejcollins/atlanta-shore/master/data/raw/spains-hall-fence.gpx')
    .on('ready', function() {
        map.fitBounds(runLayer.getBounds());
    })
    .addTo(map);
</script>
