# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pygrib

def openGrib(fname):
    grib = fname
    grbs = pygrib.open(grib)
    return grbs

def getVariable(grbs, num):
    if num == -1:
#        num = 0
        for num in grbs:
            grb = grbs.select()[num]
            print(grb)
    else:
        grb = grbs.select()[num]
        print(grb)


def displayContour(grbs, num, latmin, latmax, lonmin, lonmax):
    plt.figure(figsize=(12,8))
    
    
    grb = grbs.select()[num]
    lat,lon = grb.latlons()
    data = grb.values

    m = Basemap(projection='cyl', llcrnrlon=lonmin, \
         urcrnrlon=lonmax, llcrnrlat=latmin, urcrnrlat=latmax, \
         resolution='i')

    m.drawcoastlines()
    m.drawmapboundary()
    m.drawparallels(np.arange(latmin, latmax, 1.), labels=[1, 0, 0, 0])
    m.drawmeridians(np.arange(lonmin, lonmax, 1.), labels=[0, 0, 0, 1])
    x, y = (lon, lat)
#    data = data - 273.015
    
    im = m.contour(x,y,data,shading='faceted',cmap=plt.cm.rainbow)
        
    plt.title(grb)
    plt.clabel(im, inline=2, fontsize=18, fmt='%d')
    plt.show()

def closeWindow():
    plt.close()

if __name__ == "__main__":
   grbs = openGrib('Z__C_RJTD_20170211000000_GSM_GPV_Rgl_FD0000_grib2.bin')
#   getVariable(grbs, -1)
   displayContour(grbs, 3, 35, 37, 139, 141)
