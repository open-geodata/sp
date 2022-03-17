import os


# Set Directory
tabs_path = os.path.join('..', 'data', 'tabs')
shps_path = os.path.join('..', 'data', 'shps')
gpkg_path = os.path.join('..', 'data', 'gpkg')
zips_path = os.path.join('..', 'data', 'zips')

# Create Directory
os.makedirs(shps_path, exist_ok=True)
os.makedirs(tabs_path, exist_ok=True)
os.makedirs(gpkg_path, exist_ok=True)
os.makedirs(zips_path, exist_ok=True)



