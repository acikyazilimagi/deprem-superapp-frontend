from helpers.location_helpers import google_maps_helper, folium_helper
import os
from helpers.streamlit_helpers import streamlit_session_helper as ssh
from models import GLOBALS
import numpy as np


def GetProvinceDistrictDict():
    return GLOBALS.PROVINCE_DISTRICT_DICT


def GetCurrentLocationInfo(address=None, lat_long=None):
    current_location = google_maps_helper.GetLocationInfo(address, lat_long)
    if current_location is None:
        return GetDefaultAddress()
    else:
        return current_location


def GetDefaultAddress():
    return [os.getenv("DEFAULT_LATITUDE"), os.getenv("DEFAULT_LONGITUDE")], os.getenv("DEFAULT_PROVINCE"), os.getenv(
        "DEFAULT_DISTRICT"), os.getenv(
        "DEFAULT_ADDRESS")


def SetAddressFields(page, current_lat_long=None, current_province=None, current_district=None,
                     current_address=None):
    province_district_dict = GetProvinceDistrictDict()

    if current_lat_long is not None:
        ssh.set_session(f"{page}_latitude", str(current_lat_long[0]))
        ssh.set_session(f"{page}_longitude", str(current_lat_long[1]))
        ssh.set_session(f"{page}_map", folium_helper.CreateMap([str(i) for i in current_lat_long], is_marker=True))

    if current_province is not None:
        ssh.set_session(f"{page}_province", current_province)
        ssh.set_session(f"{page}_selectable_districts",
                        np.array(
                            province_district_dict[current_province]))

    if current_district is not None:
        ssh.set_session(f"{page}_district", current_district)

    if current_address is not None:
        ssh.set_session(f"{page}_address", current_address)
