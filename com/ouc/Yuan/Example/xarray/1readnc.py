# -*- coding: utf-8 -*-
import xarray as xr
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeat
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import matplotlib.pyplot as plt

# 数据读取
ds = xr.open_dataset('E:/python/xarray/HadISST1_SST_update.nc')
print(ds)
sst = (ds['sst']).mean(dim='time')
print(sst)

# 创建画图空间
proj = ccrs.PlateCarree() #创建投影
fig = plt.figure(figsize=(9,6)) #创建页面
ax = fig.subplots(1,1,subplot_kw={'projection':proj}) #子图

# 设置地图属性:加载国界、海岸线、河流、湖泊
ax.add_feature(cfeat.BORDERS.with_scale('50m'),linewidth=0.8,zorder=1)
ax.add_feature(cfeat.COASTLINE.with_scale('50m'),linewidth=0.6,zorder=1)
ax.add_feature(cfeat.RIVERS.with_scale('50m'),zorder=1)
ax.add_feature(cfeat.LAKES.with_scale('50m'),zorder=1)

# 设置网格点属性
gl = ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=True,linewidth=1.2,color='k',alpha=0.5,linestyle='--')
gl.xlabels_top = False # 关闭顶端标签
gl.ylabels_right = False # 关闭右端标签
gl.xformatter = LATITUDE_FORMATTER
gl.yformatter = LONGITUDE_FORMATTER
# 设置colorbar
cbar_kwargs = {
    'orientation': 'horizontal',
    'label': 'sst (℃)',
    'shrink': 0.8,
    'ticks': np.arange(-30,30+5,5)
}

# 画图
levels = np.arange(-30,30+1,5)
sst.plot.contourf(ax=ax,levels=levels,cbar_kwargs=cbar_kwargs, cmap='Spectral_r')
plt.savefig('E:/python/xarray/sst.png',dpi=300)
plt.show()
