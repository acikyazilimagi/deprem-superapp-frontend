from helpers.streamlit_helpers import streamlit_session_helper as session_helper, streamlit_helper as sh
from helpers.location_helpers import address_helper as ah
import numpy as np
from datetime import datetime


def first_page_province_changed():
    selected_province = session_helper.get_session("first_page_province")
    session_helper.set_session("first_page_selectable_districts",
                               np.array(session_helper.get_session("province_district_dict")[selected_province]))
    session_helper.set_session("first_page_district_index", 0)


def first_page_district_changed():
    selected_province = session_helper.get_session("first_page_province")
    selected_district = session_helper.get_session("first_page_district")

    address = f"{selected_province} {selected_district}"

    current_lat_long, _, _, _ = ah.GetCurrentLocationInfo(address)

    ah.SetAddressFields("first_page", current_lat_long=current_lat_long)


def first_page_address_changed():
    print(session_helper.get_session("first_page_is_address_autofill"))
    if session_helper.get_session("first_page_is_address_autofill"):
        address = session_helper.get_session("first_page_address")

        if len(address) > 5:
            current_lat_long, current_province, current_district, current_address = ah.GetCurrentLocationInfo(address)
            print(current_lat_long, current_province, current_district, current_address)

            ah.SetAddressFields("first_page", current_lat_long, current_province, current_district, current_address)
    """
        if len(st.session_state['address']) > 5:
        my_province, my_district, my_open_address, my_latlong = ah.GetCurrentLocationInfo(
            address=st.session_state.address)
        if my_latlong is not None and len(my_latlong) == 2:
            if not st.session_state.is_address_autofill:
                my_open_address = None
            sh.SetAddressFields(my_province, my_district, my_latlong, my_open_address)

    :return:
    """
    pass


def first_page_on_lat_long_button_clicked():
    pass


def first_page_on_submit_button_click(payload):
    print(session_helper.get_session("first_page_latitude"))
    print(session_helper.get_session("first_page_longitude"))
    print(payload)
    """
    diff_seconds = (datetime.now() - session_helper.get_session("first_page_message_send_date")).total_seconds()
    if diff_seconds > 120:
        if sh.ValidatePayload(payload):
            payload["zaman"] = datetime.now()
    """

    pass







def second_page_province_changed():
    selected_province = session_helper.get_session("second_page_province")
    session_helper.set_session("second_page_selectable_districts",
                               np.array(session_helper.get_session("province_district_dict")[selected_province]))
    session_helper.set_session("second_page_district_index", 0)


def second_page_district_changed():
    selected_province = session_helper.get_session("second_page_province")
    selected_district = session_helper.get_session("second_page_district")

    address = f"{selected_province} {selected_district}"

    current_lat_long, _, _, _ = ah.GetCurrentLocationInfo(address)

    ah.SetAddressFields("second_page", current_lat_long=current_lat_long)
