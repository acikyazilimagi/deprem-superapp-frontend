import streamlit as st
from helpers.location_helpers import folium_helper as fh
from helpers.streamlit_helpers import streamlit_session_helper as ssh
from helpers.location_helpers import address_helper as ah
import os


def GetSelectableDistricts(province_district_dict):
    return province_district_dict[st.session_state.province_list[0]]


def SetInitialStreamlitStates(sections):
    province_district_dict = None
    if "global" in sections:
        province_district_dict = ah.GetProvinceDistrictDict()
        if 'province_district_dict' not in st.session_state:
            ssh.set_session("province_district_dict", province_district_dict)

        if 'province_list' not in st.session_state:
            ssh.set_session("province_list", list(province_district_dict.keys()))

    if "first_page" in sections:
        if 'first_page_latitude' not in st.session_state:
            ssh.set_session("first_page_latitude", os.getenv("DEFAULT_LATITUDE"))
        if 'first_page_longitude' not in st.session_state:
            ssh.set_session("first_page_longitude", os.getenv("DEFAULT_LONGITUDE"))

        if 'first_page_province_index' not in st.session_state:
            ssh.set_session("first_page_province_index",
                            list(province_district_dict.keys()).index(os.getenv("DEFAULT_PROVINCE")))

            ssh.set_session("second_page_district_index",
                            province_district_dict[os.getenv("DEFAULT_PROVINCE")].index(os.getenv("DEFAULT_DISTRICT")))

        if 'first_page_district_index' not in st.session_state:
            ssh.set_session("first_page_district_index",
                            province_district_dict[os.getenv("DEFAULT_PROVINCE")].index(os.getenv("DEFAULT_DISTRICT")))

        if 'first_page_selectable_districts' not in st.session_state:
            ssh.set_session("first_page_selectable_districts",
                            province_district_dict[os.getenv("DEFAULT_PROVINCE")])

        if 'first_page_map' not in st.session_state:
            ssh.set_session("first_page_map", fh.CreateDefaultMap(zoom_start=15, is_marker=True))

        if 'first_page_is_success' not in st.session_state:
            ssh.set_session("first_page_is_success", False)

        if 'first_page_is_error' not in st.session_state:
            ssh.set_session("first_page_is_error", False)

        if 'first_page_is_error_message' not in st.session_state:
            ssh.set_session("first_page_is_error_message", "")

    if "second_page" in sections:
        if 'second_page_map' not in st.session_state:
            st.session_state.second_page_map = fh.CreateDefaultMap()

        if 'second_page_province_index' not in st.session_state:
            ssh.set_session("second_page_province_index",
                            list(province_district_dict.keys()).index(os.getenv("DEFAULT_PROVINCE")))

            ssh.set_session("second_page_district_index",
                            province_district_dict[os.getenv("DEFAULT_PROVINCE")].index(os.getenv("DEFAULT_DISTRICT")))

        if 'second_page_district_index' not in st.session_state:
            ssh.set_session("second_page_district_index",
                            province_district_dict[os.getenv("DEFAULT_PROVINCE")].index(os.getenv("DEFAULT_DISTRICT")))

        if 'second_page_selectable_districts' not in st.session_state:
            ssh.set_session("second_page_selectable_districts",
                            province_district_dict[os.getenv("DEFAULT_PROVINCE")])


def PopupError(page, error_message):
    ssh.set_session(f"{page}_is_error", True)
    ssh.set_session(f"{page}_is_success", False)
    ssh.set_session(f"{page}_error_message", error_message)


def PopupSuccess(page):
    ssh.set_session(f"{page}_is_success", True)
    ssh.set_session(f"{page}_is_error", False)
