# -*- coding: utf-8 -*-
import xarray as xr
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeat
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import matplotlib.pyplot as plt

# 用于创建地图相关的信息
def create_map(ax):
	# 设置地图属性
	ax.add_feature(cfeat.BORDERS.with_scale('50m'), linewidth=0.8)  # 加载分辨率为50的国界线
	ax.add_feature(cfeat.COASTLINE.with_scale('50m'), linewidth=0.6)  # 加载分辨率为50的海岸线
	ax.add_feature(cfeat.RIVERS.with_scale('50m'))  # 加载分辨率为50的河流
	ax.add_feature(cfeat.LAKES.with_scale('50m'))  # 加载分辨率为50的湖泊
	# 设置网格点属性
	gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
	                  linewidth=1.2, color='k', alpha=0.5, linestyle='--')
	gl.xlabels_top = False  # 关闭顶端的经纬度标签
	gl.ylabels_right = False  # 关闭右侧的经纬度标签
	gl.xformatter = LONGITUDE_FORMATTER  # x轴设为经度的格式
	gl.yformatter = LATITUDE_FORMATTER  # y轴设为纬度的格式
	return ax

if __name__ == '__main__':
	# 创建画图空间
	proj = ccrs.PlateCarree()
	fig, axes = plt.subplots(nrows=4,ncols=1,figsize=(9,14),subplot_kw={'projection':proj})
	ds = xr.open_dataset('EC-Interim_monthly_2018.nc')
	print(ds)
	temp = (ds['t2m']-273.15).groupby('time.season').mean('time')
	# 画图
	cbar_kwargs = {
	'label' : '2m temperature (℃)' ,
	'ticks' : np.arange(-30,30+5,5) ,
	}
	levels = np.arange(-30,30+1,1)
	for i,season in enumerate(('DJF','MAM','JJA','SON')):
		ax = create_map(axes[i])
		temp.sel(season=season).plot.contourf(ax=ax,levels=levels,cmap='Spectral_r',
			extend='both',cbar_kwargs=cbar_kwargs,transform=ccrs.PlateCarree())
		# fig.show()
	plt.savefig('4_t2m.png',dpi=300)
