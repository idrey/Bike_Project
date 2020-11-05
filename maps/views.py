from django.shortcuts import render
from .getdata import getCoordinate
from .postcmd import sendCmd
from .ctrans import wgs84_to_bd09
import json
# Create your views here.

def isInsidePolygon(pt, poly):
    c = False
    i = -1
    l = len(poly)
    j = l - 1
    while i < l - 1:
        i += 1
        # print(i, poly[i], j, poly[j])
        if ((poly[i][0] <= pt[0] and pt[0] < poly[j][0]) or (
                poly[j][0] <= pt[0] and pt[0] < poly[i][0])):
            if (pt[1] < (poly[j][1] - poly[i][1]) * (pt[0] - poly[i][0]) / (
                poly[j][0] - poly[i][0]) + poly[i][1]):
                c = not c
        j = i
    return c

def pack_point(lngs, lats):
    points = []
    l = len(lngs)
    for i in range(l):
        tmp = [lngs[i], lats[i]]
        points.append(tmp)
    return points

def index(request):
    address_longitude = [126.632753,126.637101,126.657492,126.639436]
    address_latitude = [45.749171,45.752667,45.745976, 45.745133]
    point_address = []
    is_checked = 'checked'
    longi, lati = getCoordinate()
    bd_point = wgs84_to_bd09(longi, lati)
    print(bd_point)
    print(pack_point(address_longitude, address_latitude))
    is_InPolygon = isInsidePolygon(bd_point, pack_point(address_longitude, address_latitude))
    point_address.append(longi)
    point_address.append(lati)
    print(point_address)
    v = request.POST.get('value')
    print(v)
    if v == 'on':
        sendCmd('unlock:1')
        is_checked = 'checked'
    elif v == 'off':
        if is_InPolygon:
            sendCmd('lock:1')
            print('In_Polygon')
            is_checked = ''
        else:
            sendCmd('lock:0')
            is_checked = 'checked'
    return render(request, 'maps/map.html', {
        'is_checked' : is_checked,
        'address_longitude' : json.dumps(address_longitude),
        'address_latitude' : json.dumps(address_latitude),
        'point_address' : json.dumps(point_address)
    })

def map(request):
    v = request.POST.get('value')
    if v:
        print(v)
    return render(request, 'maps/map.html')
