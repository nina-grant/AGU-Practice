print("Hello, world.")

import xarray as xr
import numpy as np

time = ['12-10-23']
data = xr.DataArray([[],[]], {'time': time, "location": 'SF'})
