import os


# Set Directory
data_path = os.path.join('..', 'data')
tabs_path = os.path.join(data_path, 'tabs')
shps_path = os.path.join(data_path, 'shps')
gpkg_path = os.path.join(data_path, 'gpkg')
zips_path = os.path.join(data_path, 'zips')
gjson_path = os.path.join(data_path, 'gjson')


# Create Directory
os.makedirs(shps_path, exist_ok=True)
os.makedirs(tabs_path, exist_ok=True)
os.makedirs(gpkg_path, exist_ok=True)
os.makedirs(zips_path, exist_ok=True)
os.makedirs(gjson_path, exist_ok=True)
