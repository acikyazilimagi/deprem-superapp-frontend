from helpers.streamlit_helpers import streamlit_helper as sh, streamlit_events as se, \
    streamlit_session_helper as session_helper
import streamlit as st
from streamlit_folium import folium_static
from dotenv import load_dotenv
from models import GLOBALS


third_page_payload = {}

def InitComponents():
    sh.SetInitialStreamlitStates(sections=["global", "third_page"])


InitComponents()


def third_page():
    st.header("Umut Ol!")

    folium_static(fig=session_helper.get_session("third_page_map"))

    third_page_payload["il"] = st.selectbox(
        label="İl [ZORUNLU]", options=session_helper.get_session("province_list"), key="third_page_province",
        on_change=se.third_page_province_changed, index=session_helper.get_session("third_page_province_index"),
    )

    third_page_payload["ilce"] = st.selectbox(
        label="İlçe [ZORUNLU]", options=session_helper.get_session("third_page_selectable_districts"),
        index=session_helper.get_session("third_page_district_index"),
        key="third_page_district", on_change=se.third_page_district_changed
    )

    third_page_payload["servis"] = st.multiselect(
        'Şu Konularda Yardım Edebilirim:',
        GLOBALS.NEEDS,
        GLOBALS.NEEDS[0])

    third_page_payload["adres"] = st.text_area(
        label="Adres [ZORUNLU]", key='third_page_address', on_change=se.third_page_address_changed
    )

    st.checkbox(label="Adresi benim için otomatik doldur", key="third_page_is_address_autofill", value=True)

    third_page_payload["isim"] = st.text_input(
        label="İsim [ZORUNLU]"
    )

    third_page_payload["telefon"] = st.text_input(
        label="Telefon numarası [OPSİYONEL]"
    )

    third_page_payload["notlar"] = st.text_area(
        label="NOT [OPSİYONEL]"
    )
    st.button("Gönder", key="third_page_submit_button", on_click=se.third_page_on_submit_button_click, args=(third_page_payload,))

    if session_helper.get_session("third_page_is_success"):
        st.success('Mesajınız alındı!', icon="✅")
    if session_helper.get_session("third_page_is_error"):
        st.error(session_helper.get_session("third_page_error_message"), icon="🚨")


third_page()