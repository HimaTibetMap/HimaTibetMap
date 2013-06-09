HimaTibetMap
===================

HimaTibetMap is an open-source database of active faults and associated features (suture zones, Cenozoic volcanic rocks) in the Indo-Asian collision zone.  It was created by Mike Taylor, An Yin, Richard Styron and Kelechi Okoronkwo, and is currently maintained by Styron.  
The database is currently available in .shp (for ArcGIS, Quantum GIS, etc.), .kml (Google Earth), .gmt (text, for plotting in Generic Mapping Tools), and .geojson (GeoJSON, which may be useful to some, and can be opened in QGIS).  The .shp format contains the most metadata.


Installation
----------------

These files are not executable and do not need to be installed.  Simply download them.


Plotting Data
----------

Google Earth
-------------

In order to import the KML version into Google Earth, open the file(s) using the program.  The files will be opened under the 'Temporary Places' folder and may be permanently stored by moving them into the 'My Places' folder.

Generic Mapping Tools
----------------------

The GMT version may be plotted using psxy with the -M flag.  Kinematics may be plotted using the -Sf flag with appropriate options.

ArcGIS
-------
The ESRI Shapefile version contains the structures, with kinematics for each structure included as attributes and as a code for use with a 'styles' file to display symbology.  The styles file was developed by Eric Cowgill at UC Davis, and is included in the HimaTibetMap-1.1_arc zipfile. To implement, right click on the file in the Table of Contents (in ArcMap), click on the Symbology tab, select Categories, and then select Match to symbols in a style.  Use the 'ltype' field.

New in version 1.1, the sutures and Cenozoic volcanic rocks are now separate shapefiles.  The Cenozoic shapefiles will be made into polygon shapefiles in a later version.

Quantum GIS
-------------

QGIS users can plot the .shp files with directions similar to the ArcGIS directions.  However at this time the use of the .style file to display kinematics is untested and may not function at all.  Caveat emptor.

References
--------------
The developers of this project are academics, and therefore depend on citations for food and water.  Therefore if you publish anything with this data, please cite us (take your pick, or do both if you're super nice):

Styron, R., Taylor, M., and Okoronkwo, K., 2010, HimaTibetMap-1.0: new ‘web-2.0’ online database of active structures from the Indo-Asian collision, Eos, vol.91 no. 20.

Taylor, Michael, and An Yin, 2009, "Active structures of the Himalayan-Tibetan orogen and their relationships to earthquake distribution, contemporary strain field, and Cenozoic volcanism." Geosphere vol. 5, no. 3, pp 199-214.


Data Sources
--------------
This project draws heavily on published work, although a good portion of it is our own interpretation of field observations, remote sensing imagery, seismicity, etc.  The file 'references.txt' lists the papers we used.

Contributions
---------------
This is an open-source project, and contributions and edits are strongly encouraged.  GitHub users may open issues or make pull requests for contributions; this is the preferred method for contributing.  However, others may simply email me ( richard.h.styron@gmail.com ) either describing an edit or sending me a new file.  No viruses, please!