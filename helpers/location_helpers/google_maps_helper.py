import os
from helpers.http_helpers import http_helper
from helpers.utility_helpers.string_helper import tr_upper


def GetLocationInfo(address=None, lat_long=None):
    base_url = os.getenv('GOOGLE_MAPS_BASE_URL')
    if lat_long is not None:
        lat_long = ','.join([str(i) for i in lat_long])

    query_params = {
        "address": address,
        "latlng": lat_long,
        "key": os.getenv('GOOGLE_MAPS_API_KEY')
    }
    r = http_helper.send_request(base_url, method="GET", query_params=query_params)
    latitude, longitude, my_province, my_district, my_open_address = None, None, None, None, None
    if r is not None:
        try:
            results = r.json()['results'][0]
            my_province = tr_upper(
                [i["long_name"] for i in results["address_components"] if "administrative_area_level_1" in i["types"]][
                    0])

            my_district = tr_upper(
                [i["long_name"] for i in results["address_components"] if
                 "sublocality" in i["types"] or "administrative_area_level_2" in i["types"]][0])

            my_open_address = results["formatted_address"]

            if lat_long is None:
                lat_long = list(results["geometry"]["location"].values())

        except:
            return None

    return lat_long, my_province, my_district, my_open_address
