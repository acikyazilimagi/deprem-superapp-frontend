import os

import folium
from folium.plugins import HeatMap

from helpers.http_helpers import http_helper


def CreateMap(my_latlong, zoom_start=17, is_marker=False):
    m = folium.Map(my_latlong, zoom_start=zoom_start)
    if is_marker:
        folium.Marker(
            my_latlong, popup="Konumum", tooltip="Konumum"
        ).add_to(m)

    return m


def CreateDefaultMap(zoom_start=17, is_marker=False):
    m = CreateMap([38.7792, 35.4572], zoom_start, is_marker)

    return m


def CreateHeatMap(lat_long_list=None, zoom_start=5, is_marker=False):
    density_map = CreateMap([38.7792, 35.4572], zoom_start, is_marker)

    if len(lat_long_list) > 0:
        HeatMap(lat_long_list, radius=15).add_to(density_map)

    return density_map


def CreateMultiMarkerMap(lat_longs):
    m = CreateDefaultMap(zoom_start=5)
    for loc in lat_longs:
        folium.Marker(loc).add_to(m)

    return m
