from helpers.streamlit_helpers import streamlit_helper as sh, streamlit_events as se, \
    streamlit_session_helper as session_helper
import streamlit as st
from streamlit_folium import folium_static
from dotenv import load_dotenv
from models import GLOBALS


third_page_payload = {}

def InitComponents():
    sh.SetInitialStreamlitStates(sections=["global", "third_page"])
    st.set_page_config(layout="wide")

InitComponents()


def third_page():
    st.header("Umut Ol!")

    folium_static(fig=session_helper.get_session("third_page_map"), width=1400, height=600)

    third_page_payload["il"] = st.sidebar.selectbox(
        label="İl [ZORUNLU]", options=session_helper.get_session("province_list"), key="third_page_province",
        on_change=se.third_page_province_changed, index=session_helper.get_session("third_page_province_index"),
    )

    third_page_payload["ilce"] = st.sidebar.selectbox(
        label="İlçe [ZORUNLU]", options=session_helper.get_session("third_page_selectable_districts"),
        index=session_helper.get_session("third_page_district_index"),
        key="third_page_district", on_change=se.third_page_district_changed
    )

    third_page_payload["servis"] = st.sidebar.multiselect(
        'Şu Konularda Yardım Edebilirim:',
        GLOBALS.NEEDS,
        GLOBALS.NEEDS[0])

    third_page_payload["adres"] = st.sidebar.text_area(
        label="Adres [ZORUNLU]", key='third_page_address', on_change=se.third_page_address_changed
    )

    st.sidebar.checkbox(label="Adresi benim için otomatik doldur", key="third_page_is_address_autofill", value=True)

    third_page_payload["isim"] = st.sidebar.text_input(
        label="İsim [ZORUNLU]"
    )

    third_page_payload["telefon"] = st.sidebar.text_input(
        label="Telefon numarası [OPSİYONEL]"
    )

    third_page_payload["notlar"] = st.sidebar.text_area(
        label="NOT [OPSİYONEL]"
    )
    st.sidebar.button("Gönder", key="third_page_submit_button", on_click=se.third_page_on_submit_button_click, args=(third_page_payload,))

    if session_helper.get_session("third_page_is_success"):
        st.sidebar.success('Mesajınız alındı!', icon="✅")
    if session_helper.get_session("third_page_is_error"):
        st.sidebar.error(session_helper.get_session("third_page_error_message"), icon="🚨")


third_page()