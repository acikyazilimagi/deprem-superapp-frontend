
from datetime import datetime

import folium
from folium.plugins import HeatMap
from models.GLOBALS import icon_map


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


def CreateMultiMarkerMap(raw_data=None):

    m = CreateDefaultMap(zoom_start=5)
    if raw_data is not None:
        for i in range(len(raw_data)):
            lat,lon = raw_data[i]["lat"],raw_data[i]["lon"]
            #if raw data does not have gereksinimler
            if "gereksinimler" not in raw_data[i]:
                a = "servis"
            else:
                a = "gereksinimler"

            if "zaman" not in raw_data[i]:
                popup_html_table = """
                <style>
                    table {
                        width: 300px;
                        font-size: 12px;
                        font-weight: bold;
                    }
                </style>
                <table>
                    <tr>
                        <th>il: </th>
                        <td>""" + str(raw_data[i]["il"]) + """</td>
                    </tr>
                    <tr>
                        <th>ilce: </th>
                        <td>""" + str(raw_data[i]["ilce"]) + """</td>
                    </tr>
                    <tr>
                        <th>adres: </th>
                        <td>""" + str(raw_data[i]["adres"]) + """</td>
                    </tr>
                    <tr>
                        <th>servisler: </th>
                        <td>""" + str(" ".join(raw_data[i][a])) + """</td>
                    </tr>
                    <tr>
                        <th>telefon: </th>
                        <td>""" + str(raw_data[i]["telefon"]) + """</td>
                    </tr>
                    <tr>
                        <th>notlar: </th>
                        <td>""" + str(raw_data[i]["notlar"]) + """</td>
                    </tr>
                </table>"""

            else:
                popup_html_table = """
                <div style='width:300px; font-size:12px; font-weight: bold;'>
                    <table>
                        <tr>
                            <th>il: </th>
                            <td>""" + str(raw_data[i]["il"]) + """</td>
                        </tr>
                        <tr>
                            <th>ilce: </th>
                            <td>""" + str(raw_data[i]["ilce"]) + """</td>
                        </tr>
                        <tr>
                            <th>adres: </th>
                            <td>""" + str(raw_data[i]["adres"]) + """</td>
                        </tr>
                        <tr>
                            <th>gereksinimler: </th>
                            <td>""" + str(" ".join(raw_data[i][a])) + """</td>
                        </tr>
                        <tr>
                            <th>telefon: </th>
                            <td>""" + str(raw_data[i]["telefon"]) + """</td>
                        </tr>
                        <tr>
                            <th>zaman: </th>
                            <td>""" + str(
                    datetime.strptime(raw_data[i]["zaman"], '%Y-%m-%dT%H:%M:%S.%f').strftime("%B %d, %H:%M:%S")) + """</td>
                        </tr>
                        <tr>
                            <th>google konum: </th>
                            <td><a target="_blank" href=""" + str(
                    f"http://maps.google.com/?ll={raw_data[i]['lat']},{raw_data[i]['lon']}") + """>google maps link</a></td>
                        </tr>
                        <tr>
                            <th>notlar: </th>
                            <td>""" + str(raw_data[i]["notlar"]) + """</td>
                        </tr>
                    </table>
                </div>"""

            icon_list = [x+" "+icon_map[x]+" " for x in raw_data[i][a]]

            # add hover text
            icon_person = folium.Icon(icon='person', prefix='fa',color='red')
            icon_house = folium.Icon(icon='home', prefix='fa')
            if a == "gereksinimler":
                folium.Marker([lat, lon], popup=popup_html_table,tooltip="<span style='font-size:16px'><strong>İhtiyaçlar:</strong>"+" ".join(icon_list)+"</span>",icon=icon_person,icon_size=(30,30)).add_to(m)

            else:
                folium.Marker([lat, lon], popup=popup_html_table,tooltip="<span style='font-size:16px'><strong>Servisler:</strong>"+" ".join(icon_list)+"</span>",icon=icon_house,icon_size=(30,30)).add_to(m)


    return m
