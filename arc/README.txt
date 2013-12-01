HimaTibetMap-1.1

by Mike Taylor, An Yin, Richard Styron, Kelechi Okoronkwo



1.  Plotting data


In order to import the KML version into Google Earth, open the file(s) using the program.  The files will be opened under the 'Temporary Places' folder and may be permanently stored by moving them into the 'My Places' folder.


The GMT version may be plotted using psxy with the -M flag.  Kinematics may be plotted using the -Sf flag with appropriate options.


The ESRI Shapefile version contains the structures, with kinematics for each structure included as attributes and as a code for use with a 'styles' file to display symbology.  The styles file was developed by Eric Cowgill at UC Davis, and is included in the HimaTibetMap-1.1_arc zipfile. To implement, right click on the file in the Table of Contents (in ArcMap), click on the Symbology tab, select Categories, and then select Match to symbols in a style.  Use the 'ltype' field.

New in version 1.1, the sutures and Cenozoic volcanic rocks are now separate shapefiles.  The Cenozoic shapefiles will be made into polygon shapefiles in a later version.





2.  Database Compilation

The major or most well-documented structures in the Indo-Asian collision zone were found through reviews of the literature (using sources listed in the next section).  Many other structures were documented during field campaigns.  The remainder are from interpretations of remote sensing imagery, primarily data from ASTER, LANDSAT, SPOT, CORONA, Google Earth, and SRTM.  The interpretation of a given fault's activity and kinematics are based on geomorphic and circumstantial evidece.  Geomorphic indications include texture of incised geomorphic surfaces, sinuosity or linearity of mountain fronts and fault scarps, triangular facets, and offset or beheaded stream channels.  Circumstantial evidence includes geomorphic relationship of features in question to proximal, well-documented structures (e.g. high topography bound by fault scarps on an offset of a strike-slip fault that may be a restraining bend bound by thrusts), or other evidence such as earthquake focal mechanisms.  A conservative approach to structure identification and interpretation was taken, and therefore confidence in all structures is high; however, the more documentation a structure has in the literature, the higher the relative confidence level is for that structure.

The database was assembled by creating features in ESRI ArcMap on top of remote sensing imagery.  Spatial precision for a structure is somewhat a function of its geomorphic expression, but is approximately several kilometers.  The database is therefore more appropriate for regional plots versus local ones.  The ESRI Shapefile version of the database was translated into other versions using the GDAL utilities (www.gdal.org).  We have picked two of the more commonly used file types for other versions, but one may translate the data into many other GIS file types using the GDAL utilities.


3.  Data sources






		
Thrust
		
Main Frontal Thrust		Lave and Avouac, 2000, 2001; Lave, et al 2005, Nakata, 1989, Lillie and Yeats, 1991
Main Pamir Thrust		Arrowsmith and Strecker, 1999; Robinson, et al., 2004b
S. Tian Shan thrust		Thompson, et al., 2002, Tapponnier and Molnar, 1979
Dauki Thrust			Das, et al., 1995
Narin Thrust			Yin, et al., 2008
Adatan thrust			Yin, et al., 2008
Oldham Fault			Bilham and England, 2001
Longriba Fault			Xu, et al., 2008
Dalong Fault			Gold, et al., 2006
		
Fold-Thrust belt			
North Qaidam Thrust Belt		Yin, et al., 2008
Makran Thrust Belt			Molnar and Tapponnier, 1975
Western Kunlun Shan thrust belt		Avouac and Peltzer, 1993
Qilian Shan – Nan Shan thrust belt	Yin, et al., 2008
Longmen Shan thrust belt		Burchfiel, et al., 1995; Kirby, et al., 2000
Burmese Fold Belt			Wang and Burchfiel, 1997
Sichuan Fold Belt			Burchfiel, et al., 1995
Naga Hills Thrust Belt			Das, et al., 1995
		
Extensional Systems		
Gurla Mandhata detachment	Murphy, et al., 2002
Shangxi Graben			Burchfiel, et al., 1991
Yinchuan Graben			Burchfiel, et al., 1991
Kongur Shan			Avouac and Peltzer, 1993, Robinson, et al., 2004b
		
Right Slip Faults		
Jiali Fault			Armijo, et al., 1986, 1989
Karakoram Fault			Murphy, et al., 2000
Herat Fault			Molnar and Tapponnier, 1975; Tapponnier, et al., 1985, Ruleman, et al., 2007
Red River Fault			Wang, et al., 1998; Leloup, et al., 1995
Talas-Fergana Fault		Thompson, et al., 2002, Tapponnier and Molnar, 1979
Sagaing Fault			Wang and Burchfiel, 1997
Irtysh Fault			Tapponnier and Molnar, 1979
Gyaring Co Fault		Armijo, et al., 1986, 1989; Taylor, et al., 2003; Taylor and Peltzer, 2006
Gaoligong Fault			Wang and Burchfiel, 1997
		
Left Slip faults		
Altyn Tagh Fault		Cowgill, et al., 2000, 2004b; Meriaux, et al., 204; 2005
Chaman Fault			Molnar and Tapponnier, 1975, Tapponnier, et al., 1981, Ruleman, et al., 2007
Bogd Fault			Tapponnier and Molnar, 1979
Gobi-Tian Shan Fault		Tapponnier and Molnar, 1979
Haiyuan Fault			Burchfiel, et al., 1991; Lassere, et al., 2001, 2002
Kunlun Fault			Yin, et al., 2008, Van der Woerd, et al., 1998, 2000, 2002
Xiangshuihe-Xiaojiang Fault	Wang, et al., 1998
Ganzi Fault			Taylor, et al., 2003; Wang and Burchfiel, 2000
Barapani-Tyrsad Fault 		Srivastava, R., and Sinha, H., 2007
Longmu Co – Gozha Co fault	Avouac and Peltzer, 1993; Taylor, et al., 2003
Karakax Fault			Avouac and Peltzer, 1993; Taylor, et al., 2003
Riganpei Co Fault		Taylor, et al., 2003
		
Sutures		
Indus-Yalu suture			Taylor, et al., 2003; Pan, et al., 2004
Bangong – Nujiang Suture		Taylor, et al., 2003; Pan, et al., 2004
Jinsha Suture				Taylor, et al., 2003; Pan, et al., 2004
Shyok Suture Zone			Taylor, et al., 2003; Pan, et al., 2004
Tanymas Suture				Arrowsmith and Strecker, 1999;
Anyimaqen-Kunlun-Muztagh Suture Zone	Yin and Harrison, 2000; Pan, et al., 2004

Volcanics			Pan, et al., 2004


Faults not named here are either taken from Taylor, et al., 2003, Taylor and Yin, 2009, field observations by Taylor, or from remote sensing interpretation.


Works Cited

Armijo, R., P. Tapponnier, and T. Han (1989), Late Cenozoic right-lateral strike-slip faulting in southern Tibet, J. geophys. Res, 94(3), 2787–2838.

Armijo, R., P. Tapponnier, J. Mercier, and H. Tong-Lin (1986), Quaternary extension in southern Tibet: Field observations and tectonic implications, Journal of Geophysical Research, 91, 13803-13872.

Arrowsmith, J. R., and M. R. Strecker (1999), Seismotectonic range-front segmentation and mountain-belt growth in the Pamir-Alai region, Kyrgyzstan (India-Eurasia collision zone), Geological Society of America Bulletin, 111(11), 1665-1683.

Avouac, J.-P., and G. Peltzer (1993), Active Tectonics in Southern Xinjiang, China: Analysis of Terrace Riser and Normal Fault Scarp Degradation Along the Hotan-Qira Fault System, J. Geophys. Res., 98.

Bilham, R., and P. England (2001), Plateau ‘pop-up’in the great 1897 Assam earthquake, Nature, 410(6830), 806-809.

Burchfiel, B., C. Zhiliang, L. Yupinc, and L. Royden (1995), Tectonics of the Longmen Shan and adjacent regions, central China, International Geology Review, 37(8), 661-735.

Burchfiel, B. C., Z. Peizhen, W. Yipeng, Z. Weiqi, S. Fangmin, D. Qidong, P. Molnar, and L. Royden (1991), Geology of the Haiyuan fault zone, Ningxia-Hui autonomous region, China, and its relation to the evolution of the northeastern margin of the Tibetan Plateau, Tectonics, 10, 1091-1110.

Cowgill, E., A. Yin, W. X. Feng, and Z. Qing (2000), Is the North Altyn fault part of a strike-slip duplex along the Altyn Tagh fault system?, Geology, 28(3), 255-258.

Cowgill, E., J. R. Arrowsmith, A. Yin, X. F. Wang, and Z. L. Chen (2004), The Akato Tagh bend along the Altyn Tagh fault, northwest Tibet 2: Active deformation and the importance of transpression and strain hardening within the Altyn Tagh system, Geological Society of America Bulletin, 116(11-12), 1443-1464.

Das, J., A. Saraf, and A. Jain (1995), Fault tectonics of the Shillong plateau and adjoining regions, north-east India using remote sensing data, International journal of remote sensing(Print), 16(9), 1633-1646.

Gold, R., E. Cowgill, X. Wang, and X. Chen (2006), Application of trishear fault-propagation folding to active reverse faults: examples from the Dalong Fault, Gansu Province, NW China, Journal of Structural Geology, 28(2), 200-219.

Kirby, E., P. Reiners, M. Krol, K. Whipple, K. Hodges, K. Farley, W. Tang, and Z. Chen (2002), Late Cenozoic evolution of the eastern margin of the Tibetan Plateau: Inferences from 40 Ar/39 Ar and (U-Th)/He thermochronology, Tectonics, 21(1), 1001.

Lasserre, C., B. Bukchin, P. Bernard, P. Tapponnier, Y. Gaudemer, A. Mostinsky, and R. Dailu (2001), Source parameters and tectonic origin of the 1996 June 1 Tianzhu (M-w=5.2) and 1995 July 21 Yongden (M-w = 5.6) earthquakes near the Haiyuan fault (Gansu, China), Geophysical Journal International, 144(1), 206-220.

Lasserre, C., Y. Gaudemer, P. Tapponnier, A. S. Meriaux, J. Van der Woerd, D. Y. Yuan, F. J. Ryerson, R. C. Finkel, and M. W. Caffee (2002), Fast late Pleistocene slip rate on the Leng Long Ling segment of the Haiyuan fault, Qinghai, China, Journal of Geophysical Research-Solid Earth, 107(B11).

Lavé, J., and J. P. Avouac (2000), Active folding of fluvial terraces across the Siwaliks Hills, Himalayas of central Nepal, J. Geophys. Res., 105.

Lavé, J., and J. Avouac (2001), Fluvial incision and tectonic uplift across the Himalayas of central Nepal, Journal of Geophysical Research-Solid Earth, 106(B11).

Leloup, P. H., R. Lacassin, P. Tapponnier, U. Scharer, Z. Dalai, L. Xiaohan, Z. Liangshang, J. Shaocheng, and P. T. Trinh (1995), The Ailao Shan-Red River shear zone (Yunnan, China), Tertiary transform boundary of Indochina, Tectonophysics, 251, 3-84.

Meriaux, A. S., F. J. Ryerson, P. Tapponnier, J. Van der Woerd, R. C. Finkel, X. W. Xu, Z. Q. Xu, and M. W. Caffee (2004), Rapid slip along the central Altyn Tagh Fault: Morphochronologic evidence from Cherchen He and Sulamu Tagh, Journal of Geophysical Research-Solid Earth, 109(B6), B06401, doi:06410.01029/02003JB002558.

Meriaux, A. S., et al. (2005), The Aksay segment of the northern Altyn Tagh fault: Tectonic geomorphology, landscape evolution, and Holocene slip rate, Journal of Geophysical Research-Solid Earth, 110(B4), 32.

Molnar, P., and P. Tapponnier (1975), Cenozoic Tectonics of Asia: Effects of a Continental Collision: Features of recent continental tectonics in Asia can be interpreted as results of the India-Eurasia collision, Science, 189(4201), 419.

Murphy, M., A. Yin, P. Kapp, T. Harrison, C. Manning, F. Ryerson, D. Lin, and G. Jinghui (2002), Structural evolution of the Gurla Mandhata detachment system, southwest Tibet: Implications for the eastward extent of the Karakoram fault system, Geological Society of America Bulletin, 114(4), 428.

Murphy, M. A., and P. Copeland (2005), Transtensional deformation in the central Himalaya and its role in accommodating growth of the Himalayan orogen, Tectonics, 24.

Murphy, M. A., A. Yin, P. Kapp, T. M. Harrison, D. Lin, and J. H. Guo (2000), Southward propagation of the Karakoram fault system, southwest Tibet: Timing and magnitude of slip, Geology, 28(5), 451-454.

Nakata, T. (1989), Active faults of the Himalaya of India and Nepal, Tectonics of the western Himalayas: Geological Society of America Special Paper, 232, 243–264.

Pan, G., J. Ding, D. Yao, and L. Wang (2004), Geological Map of the Qinghai-Xizang (Tibet) Plateau and Adjacent Areas, Chengdu Cartographic Publishing House, Chengdu.

Robinson, A. C., A. Yin, C. E. Manning, T. M. Harrison, S.-H. Zhang, and X.-F. Wang (2004), Tectonic evolution of the northeastern Pamir: Constraints from the northern portion of the Cenozoic Kongur Shan extensional system, western China, Geological Society of America Bulletin, 116(7-8), 953-973.

Ruleman, C., A. Crone, M. Machette, K. Haller, K. Rukstales, and R. Geological Survey, VA D 1: 20070000 Map and Database of Probable and Possible Quaternary Faults in AfghanistanRep., United States Geological Survey.

Srivastava, R., and A. Sinha (2007), Nd and Sr isotope systematics and geochemistry of a plume-related Early Cretaceous alkaline-mafic-ultramafic igneous complex from Jasra, Shillong plateau, northeastern India, Geological Society of America Special Papers, 430, 815.

Tapponnier, P., and P. Molnar (1979), ACTIVE FAULTING AND CENOZOIC TECTONICS OF THE TIEN SHAN, MONGOLIA, AND BAYKAL REGIONS, J. Geophys. Res., 84.

Tapponnier, P., M. Mattauer, F. Proust, and C. Cassaigneau (1981), Mesozoic ophiolites, sutures, and large-sale tectonic moevements in Afghanistan, Earth and Planetary Science Letters, 52, 355-371.

Taylor, M., and G. Peltzer (2006), Current slip rates on conjugate strike-slip faults in central Tibet using synthetic aperture radar interferometry, J. geophys. Res, 111.

Taylor, M., A. Yin, F. Ryerson, P. Kapp, and L. Ding (2003), Conjugate strike-slip faulting along the Bangong-Nujiang suture zone accommodates coeval east-west extension and north-south shortening in the interior of the Tibetan Plateau, Tectonics, 22(4), 1044.

Thompson, S. C., R. J. Weldon, C. M. Rubin, K. Abdrakhmatov, P. Molnar, and G. W. Berger (2002), Late Quaternary slip rates across the central Tien Shan, Kyrgyzstan, central Asia, J. Geophys. Res., 107.

Van der Woerd, J., F. J. Ryerson, P. Tapponnier, Y. Gaudemer, R. Finkel, A. S. Meriaux, M. Caffee, Z. Guoguang, and H. Qunlu (1998), Holocene left-slip rate determined by cosmogenic surface dating on the Xidatan segment of the Kunlun fault (Qinghai, China), Geology, 26(8), 695-698.

Van der Woerd, J., F. J. Ryerson, P. Tapponnier, A. S. Meriaux, Y. Gaudemer, B. Meyer, R. C. Finkel, M. W. Caffee, G. G. Zhao, and Z. Q. Xu (2000), Uniform Slip-Rate along the Kunlun Fault: Implications for seismic behaviour and large-scale tectonics, Geophysical Research Letters, 27(16), 2353-2356.

Van Der Woerd, J., P. Tapponnier, F. J. Ryerson, A. S. Meriaux, B. Meyer, Y. Gaudemer, R. C. Finkel, M. W. Caffee, G. G. Zhao, and Z. Q. Xu (2002), Uniform postglacial slip-rate along the central 600 km of the Kunlun Fault (Tibet), from Al-26, Be-10, and C-14 dating of riser offsets, and climatic origin of the regional morphology, Geophysical Journal International, 148(3), 356-388.

Wang, E., and B. C. Burchfiel (1997), Interpretation of Cenozoic tectonics in the right-lateral accommodation zone between the Ailao Shan shear zone and the eastern Himalayan syntaxis, International Geology Review, 39, 191-219.

Wang, E., and B. C. Burchfiel (2000), Late Cenozoic to Holocene deformation in southwestern Sichuan and adjacent Yunnan, China, and its role in formation of the southeastern part of the Tibetan plateau, GSA Bulletin, 112(3), 413-423.

Wang, E., C. Burchfiel, L. Royden, L. Liangzhong, L. Wenxin, and C. Zhiliong (1998), Late Cenozoic Xianshuihe-Xiaojiang Red River and Dali fault systems of southern Sichuan and central Yunnan, China, GSA Special Paper, 327, 108.

Xu, X., X. Wen, G. Chen, and G. Yu (2008), Discovery of the Longriba fault zone in eastern Bayan Har block, China and its tectonic implication, Science in China Series D: Earth Sciences, 51(9), 1209-1223.

Yeats, R. S., and R. J. Lillie (1991), Contemporary Tectonics of the Himalayan Frontal Fault System - Folds, Blind Thrusts and the 1905 Kangra Earthquake, Journal of Structural Geology, 13(2), 215-225.

Yin, A., and T. M. Harrison (2000), Geologic evolution of the Himalayan-Tibetan orogen, Annual Review of Earth and Planetary Science, 28, 211-280.

Yin, A., Y. Dang, L. Wang, W. Jiang, S. Zhou, X. Chen, G. Gehrels, and M. McRivette (2008), Cenozoic tectonic evolution of Qaidam basin and its surrounding regions (Part 1): The southern Qilian Shan-Nan Shan thrust belt and northern Qaidam basin, Geological Society of America Bulletin, 120(7-8), 813.

