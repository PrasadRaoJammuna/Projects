import os
from django.contrib.gis.utils import LayerMapping
from .models import Counties

# Auto-generated `LayerMapping` dictionary for counties model
counties_mapping = {
    'counties': 'Counties',
    'codes': 'Codes',
    'cty_code': 'Cty_CODE',
    'dis': 'dis',
    'geom': 'MULTIPOLYGON',
}

county_shp = os.path.join(os.path.dirname(__file__),'data/counties.shp')

def run(verbose=True):
    lm = LayerMapping(Counties,county_shp,mapping=counties_mapping,transform=False,encoding='iso-8859-1')
    lm.save(strict=True,verbose=verbose)