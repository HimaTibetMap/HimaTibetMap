"""
to be run from the 'HimaTibetMap' directory.
Takes the shapefile as the 'master' file and rewrites/updates
other file types from it.
"""


import subprocess
import numpy as np
import json


repo_dir = './'
htm_arc = repo_dir + 'arc/HimaTibetMap.shp' 
htm_json = repo_dir + 'geojson/HimaTibetMap.geojson'


# copy shp to geojson
subprocess.call('rm {}'.format(htm_json), shell=True)

subprocess.call('ogr2ogr -f "GeoJSON" {} {}'.format(htm_json, htm_arc),
                shell=True)

# make scratch directory, then make geojson files for each structure type
# by querying the all_structures geojson.  Then we can convert these
# fault-type-specific geojson files into other file types.

htm_geo = json.load(open(htm_json) )
type_list = []

for i, feat in enumerate( htm_geo['features'] ):
    type_list.append(feat['properties']['ltype'] )

ype_array = np.array(type_list)

thrust_list = []
thrust_approx_list = []
thrust_inferred_list = []
normal_list = []
normal_approx_list = []
dextral_list = []
dextral_approx_list = []
sinistral_list = []
sinistral_approx_list = []
anticline_list = []
anticline_approx_list = []
syncline_list = []
syncline_approx_list = []
leftover_list = []


for feat in htm_geo['features']:
    
    if feat['properties']['ltype'] == u'1111':
        thrust_list.append( feat)
    
    elif feat['properties']['ltype'] == u'1121':
        thrust_approx_list.append( feat)
    
    elif feat['properties']['ltype'] == u'1131':
        thrust_inferred_list.append( feat)
    
    elif feat['properties']['ltype'] == u'1211':
        normal_list.append( feat)
    
    elif feat['properties']['ltype'] == u'1221':
        normal_approx_list.append( feat)
    
    elif feat['properties']['ltype'] == u'1311':
        dextral_list.append( feat)
    
    elif feat['properties']['ltype'] == u'1321':
        dextral_approx_list.append( feat)
    
    elif feat['properties']['ltype'] == u'1411':
        sinistral_list.append( feat)
    
    elif feat['properties']['ltype'] == u'1421':
        sinistral_approx_list.append( feat)
    
    elif feat['properties']['ltype'] == u'1611':
        anticline_list.append( feat)
    
    elif feat['properties']['ltype'] == u'1621':
        anticline_approx_list.append( feat)
    
    elif feat['properties']['ltype'] == u'1711':
        syncline_list.append( feat)
    
    elif feat['properties']['ltype'] == u'1721':
        syncline_approx_list.append( feat)
    
    else:
        leftover_list.append( feat)


thrust_json = {u'features': thrust_list,
               u'type': u'FeatureCollection'}

thrust_approximate_json = {u'features': thrust_approx_list,
               u'type': u'FeatureCollection'}

thrust_inferred_json = {u'features': thrust_inferred_list,
               u'type': u'FeatureCollection'}

normal_json = {u'features': normal_list,
               u'type': u'FeatureCollection'}

normal_approximate_json = {u'features': normal_approx_list,
               u'type': u'FeatureCollection'}

dextral_json = {u'features': dextral_list,
               u'type': u'FeatureCollection'}

dextral_approximate_json = {u'features': dextral_approx_list,
               u'type': u'FeatureCollection'}

sinistral_json = {u'features': sinistral_list,
               u'type': u'FeatureCollection'}

sinistral_approximate_json = {u'features': sinistral_approx_list,
               u'type': u'FeatureCollection'}

anticline_json = {u'features': anticline_list,
               u'type': u'FeatureCollection'}

anticline_approximate_json = {u'features': anticline_approx_list,
               u'type': u'FeatureCollection'}

syncline_json = {u'features': syncline_list,
               u'type': u'FeatureCollection'}

syncline_approximate_json = {u'features': syncline_approx_list,
               u'type': u'FeatureCollection'}



subprocess.call('mkdir scratch', shell=True)


types_list = [
              'thrust',
              'thrust_approximate',
              'thrust_inferred',
              'normal',
              'normal_approximate',
              'dextral',
              'dextral_approximate',
              'sinistral',
              'sinistral_approximate',
              'anticline',
              'anticline_approximate',
              'syncline',
              'syncline_approximate'
              ]

json_dict = {'thrust_json' : thrust_json, 
             'thrust_approximate_json' : thrust_approximate_json,
             'thrust_inferred_json' : thrust_inferred_json,
             'normal_json' : normal_json,
             'normal_approximate_json' : normal_approximate_json,
             'dextral_json' : dextral_json,
             'dextral_approximate_json' : dextral_approximate_json,
             'sinistral_json' : sinistral_json,
             'sinistral_approximate_json' : sinistral_approximate_json,
             'anticline_json' : anticline_json,
             'anticline_approximate_json' : anticline_approximate_json,
             'syncline_json' : syncline_json,
             'syncline_approximate_json' : syncline_approximate_json
             }

for ftype in types_list:
    with open( 'scratch/{}.geojson'.format(ftype), 'w') as f:
        json.dump( json_dict['{}_json'.format(ftype)], f)


for ftype in types_list:
    print('{}.geojson'.format(ftype))
    subprocess.call('ogr2ogr -f "KML" kml/{}.kml scratch/{}.geojson'.format(
                                                     ftype, ftype), shell=True)
    subprocess.call('ogr2ogr -f "GMT" gmt/{}.gmt scratch/{}.geojson'.format(
                                                     ftype, ftype), shell=True)
