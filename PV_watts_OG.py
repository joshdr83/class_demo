import sys, json, requests
from urllib.request import urlopen

# input parameters
lat = sys.argv[1]
long = sys.argv[2]
size = sys.argv[3]

# url generator
nrel_api_key = 'kVTh5O88nbYohgldbB92JC17TL4UzxwauQo1x2Ha'

url = 'https://developer.nrel.gov/api/pvwatts/v6.json?api_key=%s&lat=%s&lon=%s&system_capacity=%s&azimuth=180&tilt=40&array_type=1&module_type=1&losses=10' % (nrel_api_key, lat, long, size)

## add catch for bad locations
if(requests.get(url).status_code != 200):
    print('You appear to have chosen a location without data! Maybe try again?')
    exit()

response = urlopen(url)
pv_out = json.loads(response.read())

location = pv_out['station_info']['state']
gen = round(pv_out['outputs']['ac_annual'])

print('A %s kW solar PV array in %s should output about %s kWh per year!' % (size, location, gen))