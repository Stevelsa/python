# -*- coding: utf-8 -*-
import xarray as xr
import arrow
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeat
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import matplotlib.pyplot as plt

# ds = xr.open_dataset('E:/python/nc/HadISST1_SST_update.nc')
# print(ds)
# print(' ')

# sst = ds['sst']
# print(sst)
# print(' ')


# # 根据位置索引，只对DataArray有效，对DataSet无效。
# # 1 通过数字索引
# print(sst[:,1,1])
# print(' ')

# # 通过标签索引
# print(sst.loc[:,89.5,177.5])
# print(' ')

# # 根据维度名字索引，对DataArray和DataSet都有效
# # 1 通过数字索引
# print(ds.isel(longitude=1,time=0))
# print(' ')

# # 2 通过标签索引
# print(ds.sel(longitude=117.5,time='2020-01-16'))
# print(' ')

# 用于创建地图相关的信息
def map():
	# 创建画图空间
	proj = ccrs.PlateCarree() # 创建坐标系
	fig = plt.figure(figsize=(9,6)) # 创建页面
	ax = fig.subplots(1, 1, subplot_kw={'projection':proj}) # 创建子图
	# 设置地图属性
	ax.add_feature(cfeat.BORDERS.with_scale('50m'),linewidth=0.8,zorder=1) # 国界线
	ax.add_feature(cfeat.COASTLINE.with_scale('50m'),linewidth=0.6,zorder=1) # 海岸线
	ax.add_feature(cfeat.RIVERS.with_scale('50m'),zorder=1) # 河流
	ax.add_feature(cfeat.LAKES.with_scale('50m'),zorder=1) # 湖泊
	# 设置网格点属性
	gl = ax.gridlines(crs=ccrs.PlateCarree(),draw_labels=True,linewidth=1.2,color='k',alpha=0.5,linestyle='--')
	gl.xlabels_top = False   # 关闭顶端的经纬度标签
	gl.ylabels_right = False # 关闭右端的经纬度标签
	gl.xformatter = LONGITUDE_FORMATTER # x轴设为经度的格式
	gl.yformatter = LATITUDE_FORMATTER  # y轴设为纬度的格式
	return fig,ax

# 生成地图
fig, ax = map()
# 数据读取
ds = xr.open_dataset('E:/python/xarray/HadISST1_SST_update.nc')
lat = ds.latitude
lon = ds.longitude
time = ds.time
sst = (ds['sst'] + 1.0)
# 区域选择
lon_range = lon[(lon>70) & (lon<140)]
lat_range = lat[(lat>0)  & (lat<60)]
sst_region = sst.sel(longitude=lon_range,latitude=lat_range,time='2020-01-16')
print(sst_region)
# 画图
cbar_kwargs = {
	'label'  : 'sst (℃)', 
	'ticks'  : np.arange(-30,30+5,5),
	'shrink' : 0.8 ,
	'orientation' : 'horizontal'
	}
levels = np.arange(-30,30+1,1)
sst_region[0,:,:,].plot.contourf(ax=ax,levels=levels,cmap='Spectral_r',cbar_kwargs=cbar_kwargs)#,extend='both',transform=ccrs.PlateCarree)
plt.savefig('E:/python/xarray/sst_region.png',dpi=300)
plt.show()
