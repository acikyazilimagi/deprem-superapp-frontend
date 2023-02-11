import streamlit as st

from helpers.http_helpers import http_helper
from helpers.location_helpers import folium_helper as fh
from helpers.streamlit_helpers import streamlit_session_helper as ssh
from helpers.location_helpers import address_helper as ah
import os
from datetime import datetime, timedelta

from models import GLOBALS
from services import record_service


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

            ssh.set_session("first_page_district_index",
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

        if 'first_page_message_send_date' not in st.session_state:
            ssh.set_session("first_page_message_send_date", datetime.now() - timedelta(minutes=5))

    if "second_page" in sections:
        if 'second_page_province_list' not in st.session_state:
            ssh.set_session("second_page_province_list", ["TÜMÜ"] + list(province_district_dict.keys()))

        if 'second_page_selected_option' not in st.session_state:
            ssh.set_session('second_page_selected_option', 'caller')

        if 'second_page_header' not in st.session_state:
            ssh.set_session('second_page_header', GLOBALS.CALLER_MAP_HEADER)

        if 'second_page_map' not in st.session_state:
            raw_lat_longs = record_service.GetRawLocationDataForMap(is_first_time=True)
            ssh.set_session("second_page_map", fh.CreateMultiMarkerMap(raw_data=raw_lat_longs))

        if 'second_page_last_call_records' not in st.session_state:
            SetCallRecordsState()

        if 'second_page_is_filtered' not in st.session_state:
            ssh.set_session("is_filtered", False)

        if 'second_page_province_index' not in st.session_state:
            ssh.set_session("second_page_province_index", list(province_district_dict).index("HATAY")+1)

        if 'second_page_district_index' not in st.session_state:
            ssh.set_session("second_page_district_index", 0)

        if 'second_page_selectable_districts' not in st.session_state:
            ssh.set_session("second_page_selectable_districts",
                            ["TÜMÜ"])

        if 'second_page_start_date_value' not in st.session_state:
            ssh.set_session("second_page_start_date_value", datetime.today())

        if 'second_page_end_date_value' not in st.session_state:
            ssh.set_session("second_page_end_date_value", datetime.today() + timedelta(days=2))

        if 'second_page_min_end_data_filter_value' not in st.session_state:
            ssh.set_session("second_page_min_end_data_filter_value", None)

        if 'second_page_is_filtered' not in st.session_state:
            ssh.set_session("second_page_is_filtered", False)

    if "third_page" in sections:
        if 'third_page_latitude' not in st.session_state:
            ssh.set_session("third_page_latitude", os.getenv("DEFAULT_LATITUDE"))
        if 'third_page_longitude' not in st.session_state:
            ssh.set_session("third_page_longitude", os.getenv("DEFAULT_LONGITUDE"))

        if 'third_page_province_index' not in st.session_state:
            ssh.set_session("third_page_province_index",
                            list(province_district_dict.keys()).index(os.getenv("DEFAULT_PROVINCE")))

            ssh.set_session("third_page_district_index",
                            province_district_dict[os.getenv("DEFAULT_PROVINCE")].index(os.getenv("DEFAULT_DISTRICT")))

        if 'third_page_district_index' not in st.session_state:
            ssh.set_session("third_page_district_index",
                            province_district_dict[os.getenv("DEFAULT_PROVINCE")].index(os.getenv("DEFAULT_DISTRICT")))

        if 'third_page_selectable_districts' not in st.session_state:
            ssh.set_session("third_page_selectable_districts",
                            province_district_dict[os.getenv("DEFAULT_PROVINCE")])

        if 'third_page_map' not in st.session_state:
            ssh.set_session("third_page_map", fh.CreateDefaultMap(zoom_start=15, is_marker=True))

        if 'third_page_is_success' not in st.session_state:
            ssh.set_session("third_page_is_success", False)

        if 'third_page_is_error' not in st.session_state:
            ssh.set_session("third_page_is_error", False)

        if 'third_page_is_error_message' not in st.session_state:
            ssh.set_session("third_page_is_error_message", "")

        if 'third_page_message_send_date' not in st.session_state:
            ssh.set_session("third_page_message_send_date", datetime.now() - timedelta(minutes=5))


def GetCallRecordsDetails():
    return ssh.get_session("second_page_last_call_records")


def SetCallRecordsState(page_size=GLOBALS.PAGE_SIZE, page=0, province=None, district=None, name=None, needs=None,
                        notes=None,
                        phone=None, start_date=None,
                        end_date=None):
    ssh.set_session("current_page", page)

    if ssh.get_session('second_page_selected_option') == 'caller':
        last_records = record_service.GetCallRecords(province, district, name, needs, notes, phone, start_date,
                                                     end_date)
    else:
        last_records = record_service.GetHelperRecords(province, district, name, needs, notes, phone, start_date,
                                                       end_date)
    last_records_list = record_service.FillCallRecordString(
        last_records[page * page_size:(page * page_size) + page_size])

    ssh.set_session("second_page_last_call_record_count", len(last_records))
    ssh.set_session("second_page_last_call_records", last_records_list)
    ssh.set_session("second_page_last_call_records_raw", last_records)


def PopupError(page, error_message):
    ssh.set_session(f"{page}_is_error", True)
    ssh.set_session(f"{page}_is_success", False)
    ssh.set_session(f"{page}_error_message", error_message)


def PopupSuccess(page):
    ssh.set_session(f"{page}_is_success", True)
    ssh.set_session(f"{page}_is_error", False)


def SetCallDataRecordStates():
    pass
