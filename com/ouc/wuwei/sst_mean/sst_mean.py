import xarray as xr
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeat
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import matplotlib.pyplot as plt
#
ds = xr.open_dataset('E:/python_test/HadISST1_SST_update.nc')
# print(ds)
sst = (ds['sst'])
sst.attrs['units'] = 'deg C'
# sstJan = sst.loc['2020-01-16T12:00:00']
sstJan = sst.mean(dim='time')
lon=(ds['longitude'])
lat=(ds['latitude'])
#
proj = ccrs.PlateCarree()
fig = plt.figure(figsize=(9,6))
ax = fig.subplots(1, 1, subplot_kw={'projection':proj})
#
ax.add_feature(cfeat.BORDERS.with_scale('50m'), linewidth=0.8, zorder=1)
ax.add_feature(cfeat.COASTLINE.with_scale('50m'), linewidth=0.6, zorder=1)
#ax.add_feature(cfeat.RIVERS.with_scale('50m'), zorder=1)
#ax.add_feature(cfeat.LAKES.with_scale('50m'), zorder=1)
#
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, 
    linewidth=1.2, color='k', alpha=0.5, linestyle='--')
# gl.xlabels_top = False
# gl.ylabels_right = False
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
#
cbar_kwargs = {
    'orientation': 'horizontal',
    'label': '2m temperature (C)',
    'shrink': 0.8,
    'ticks': np.arange(-30, 30+5, 5)
}
#
levels = np.arange(-30, 30+1, 1)
cs = sstJan.plot.contourf(ax=ax, levels=levels,cmap='Spectral_r',cbar_kwargs=cbar_kwargs,transform=ccrs.PlateCarree())
plt.savefig('E:/python_test/sstmean.png',dpi=300)
#plt.show()
