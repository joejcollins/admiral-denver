---
title: QGIS Setup Notes
---

# QGis Setup Notes

Using QGIS version 3.4.3-Madeira

## Install QuickMapServices

* Plugins > Manage and Install Plugins...
    * QuickMapService
    * Install Plugin
* Close
* Web > QuickMapServices > Settings
    * More services
    * Get contributed pack
    * Save
* Last version onf contrib pack was downloaded!
    * OK
* Visibility
    * nasa (ticked)
    * bing (ticked)
    * google (ticked)
    * mapbox (ticked)
    * all others (un ticked)
    * Save

## Install TomBio tools

* Plugins > Manage and Install Plugins...
    * TomBio tools
    * Install Plugin
* Close

## Locate the survey area

* Change CRS (Coordinate Reference System) to EPSG:4326 - WGS 84 (bottom right hand corner of the window)
* Web > QuickMapServices > Bing > Bing Map
* Zoom in on the area

## To Create the random points within a polygon

* Layer > Create Layer > New Shapefile Layer...
    * Filename `C:\whereever\the\project\is\boundary.shp`
    * Geometry type `polygon`
    * OK
* Select the boundary layer (left click)
* Layer > Toggle Editing (= on)
* Edit > Add Polygon Feature
* Mark boundary (left click) and finish with right click
    * OK (leave id as `NULL`)
* Layer > Toggle Editing (= off)
* Do you want to save the changes to layer boundary?
    * Save
* Edit > Select > Select Feature(s)
* Click on the polygon
* Vector > Research Tools > Random Points Inside Polygons
    * Expression `60` (= the number of points you want)
    * Minimum distance between points `10 meters`
    * Run
    * Close

### Export GPX points for use in View Ranger

* Right click on the random points layer
* Export > Save Features As...
    * Format `GPs eXchange Format GPX`
    * Filename `C:\wherever\the\project\is\points.gpx`
    * CRS `EPSG:4326 - WGS 84`
    * Add saved file to map (un ticked)
    * GPX_USE_EXTENSIONS `YES`
    * OK

The file should look something like this:

```xml
<?xml version="1.0"?>
<gpx version="1.1" creator="GDAL 2.4.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ogr="http://osgeo.org/gdal" xmlns="http://www.topografix.com/GPX/1/1" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd">
<metadata><bounds minlat="52.186767066829788" minlon="-1.128193888182918" maxlat="52.193258182429538" maxlon="-1.117239786388285"/></metadata>
<wpt lat="52.189190527945314" lon="-1.122703264375532">
  <extensions>
    <ogr:id>0</ogr:id>
  </extensions>
</wpt>
<wpt lat="52.190683732326015" lon="-1.124903206001818">
  <extensions>
    <ogr:id>1</ogr:id>
  </extensions>
</wpt>
<wpt lat="52.18855928606613" lon="-1.12247621327738">
  <extensions>
    <ogr:id>2</ogr:id>
  </extensions>
</wpt>
<wpt lat="52.190158618187283" lon="-1.120695743211964">
  <extensions>
    <ogr:id>3</ogr:id>
  </extensions>
</wpt>
```

### Export CSV XY to convert to grid references with sheet numbers

Don't know why this isn't available in QGis, maybe I am missing something.

* Right click on the random points layer
* Export > Save Features As...
    * Format `Comma Separated Value CSV`
    * Filename `C:\wherever\the\project\is\points.csv`
    * CRS `EPSG:27700 - OSGB 1936`
    * Add saved file to map (un ticked)
    * Layer Option, CREATE_CSVT `YES`
    * Layer Option, GEOMETRY `AS_XY`
    * Layer Option, SEPARATOR `COMMA`
    * OK

The file should look something like this (12 figure grid references with spurious precision):

```csv
Y,X,id,
254912.2810871,460070.769246927,"0"
255076.548472869,459918.375857874,"1"
254842.258012982,460087.139992674,"2"
255021.620004009,460206.699737778,"3"
254793.89340851,459817.585632391,"4"
254987.211709348,460410.746274626,"5"
255032.448489482,460043.630676199,"6"
255366.670451529,460317.504679373,"7"
255106.919742886,460166.875878207,"8"
```

### Export boundary for reference purposes

A polygon can't be exported as GPX so it needs to be converted to a `track` to be exported.

* Select the boundary layer (left click)
* Edit > Select > Select Feature(s)
* Click on the polygon
* Vector > Geometry Tools > Polygons to Lines
    * Selected features only (ticked)
    * Run
    * Close
* Right click the new line layer
* Export > Save Features As...
    * File name `C:\whereever\the\project\is\boundary.gpx`
    * CRS `EPSG:4326 - WGS 84`
    * Add saved file to map (un ticked)
    * GPX_USE_EXTENSIONS `YES`
    * FORCE_GPX_TRACK `YES`

The resulting file should look like this:

```xml
<?xml version="1.0"?>
<gpx version="1.1" creator="GDAL 2.4.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ogr="http://osgeo.org/gdal" xmlns="http://www.topografix.com/GPX/1/1" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd">
<metadata><bounds minlat="52.679782899781813" minlon="-2.679492437047489" maxlat="52.695697527520039" maxlon="-2.650486284870098"/></metadata>
<trk>
  <extensions>
  </extensions>
  <trkseg>
    <trkpt lat="52.690123302974932" lon="-2.677763072961032">
    </trkpt>
    <trkpt lat="52.691600303568372" lon="-2.669037645070273">
    </trkpt>
    <trkpt lat="52.693648963609128" lon="-2.667622710817716">
    </trkpt>
```

### Import boundary GPX and convert to polygon

*
