# -*- coding: utf-8 -*-
import xarray as xr
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeat
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import matplotlib.pyplot as plt


def mask(ds, label='land'):
	landsea = xr.open_dataset('E:/python/xarray/landsea.nc')
	landsea = landsea['lsm']
	# del landsea["time"]
	# --ds和地形数据分辨率不一致，需将地形数据插值
	landsea = landsea.interp(latitude=ds.latitude.values,longitude=ds.longitude.values)
	# --利用地形遮盖海陆数据
	ds.coords['mask'] = (('latitude','longitude'), landsea.values[0,:,:])
	# print(ds.mask)
	if label == 'land':
		ds = ds.where(ds.mask < 0.8)
	elif label == 'ocean':
		ds = ds.where(ds.mask > 0.2)
	return ds

# 用于创建地图相关的信息
def create_map():
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

if __name__ == '__main__':
	# 数据读取及时间平均处理
	fig, ax = create_map()
	ds = xr.open_dataset('E:/python/xarray/HadISST1_SST_update.nc')
	lat = ds.latitude
	lon = ds.longitude
	time = ds.time
	sst = (ds['sst'])
	# 区域选择
	lon_range = lon[(lon>70) & (lon<140)]
	lat_range = lat[(lat>0)  & (lat<60)]
	sst_region = sst.sel(longitude=lon_range,latitude=lat_range,time='2020-01-16')

	sst_mask = mask(sst_region,'ocean')
	print(sst_mask)
	# 画图
	cbar_kwargs = {
	'label' : 'sst (℃)' ,
	'ticks' : np.arange(-30,30+5,5) ,
	'shrink' : 0.8 ,
	'orientation' : 'horizontal'
	}
	levels = np.arange(-30,30+1,1)
	sst_mask[0,:,:].plot.contourf(ax=ax,levels=levels,cmap='Spectral_r',cbar_kwargs=cbar_kwargs)
	plt.savefig('E:/python/xarray/3_sst_make.png',dpi=300)
	plt.show()




