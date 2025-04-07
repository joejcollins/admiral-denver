---
layout: default
title: Data Entry
parent: Data
---

* Use a `csv` file so you can edit with Excel.
* Three columns, key, value and comment.

```csv
quadrat,9,Light covering of snow
waypoint,1,
grid_reference,TL6787633142,
photo_up,P2010002,
photo_down,P2010003,
wetness,1,
canopy,95,
species,Mercurialis perennis,
,Urtica dioica,
,Silene dioica,
,Fagus sylvatica,
,Sambucus nigra,
,Glechoma hederacea,
,Acer campestre,
,Kindbergia praelonga,
,Brachythecium rutabulum,
.
.
.
```

The `make_dataset.py` will process this into rows for each species record.

```csv
date,quadrat,waypoint,grid_reference,photo_up,photo_down,wetness,canopy,species,comments
2019-02-01,9,1,TL6787633142,P2010002,P2010003,1,95,Mercurialis perennis,Light covering of snow
2019-02-01,9,1,TL6787633142,P2010002,P2010003,1,95,Urtica dioica,Light covering of snow
2019-02-01,9,1,TL6787633142,P2010002,P2010003,1,95,Silene dioica,Light covering of snow
2019-02-01,9,1,TL6787633142,P2010002,P2010003,1,95,Fagus sylvatica,Light covering of snow
2019-02-01,9,1,TL6787633142,P2010002,P2010003,1,95,Sambucus nigra,Light covering of snow
2019-02-01,9,1,TL6787633142,P2010002,P2010003,1,95,Glechoma hederacea,Light covering of snow
2019-02-01,9,1,TL6787633142,P2010002,P2010003,1,95,Acer campestre,Light covering of snow
2019-02-01,9,1,TL6787633142,P2010002,P2010003,1,95,Kindbergia praelonga,Light covering of snow
2019-02-01,9,1,TL6787633142,P2010002,P2010003,1,95,Brachythecium rutabulum,Light covering of snow
```
