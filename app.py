from helpers.streamlit_helpers import streamlit_helper as sh, streamlit_events as se, \
    streamlit_session_helper as session_helper
from pages.second_page import second_page
import streamlit as st
from streamlit_folium import folium_static
from dotenv import load_dotenv

load_dotenv()

payload = {}


def InitComponents():
    sh.SetInitialStreamlitStates(sections=["global", "first_page"])


InitComponents()


def first_page():
    st.header("Yardım Çağrısında Bulun!")

    folium_static(fig=session_helper.get_session("first_page_map"))

    # payload["lat"] = st.text_input("Enlem (Latitude) [ZORUNLU]", key="first_page_latitude")

    # payload["lon"] = st.text_input("Boylam (Longitude) [ZORUNLU]", key="first_page_longitude")

    # st.button("Enlem ve Boylam'a göre Arama Yap", key="first_page_lat_long_button",
    #           on_click=se.first_page_on_lat_long_button_clicked)

    payload["il"] = st.selectbox(
        label="İl [ZORUNLU]", options=session_helper.get_session("province_list"), key="first_page_province",
        on_change=se.first_page_province_changed, index=session_helper.get_session("first_page_province_index"),
    )

    payload["ilce"] = st.selectbox(
        label="İlçe [ZORUNLU]", options=session_helper.get_session("first_page_selectable_districts"),
        index=session_helper.get_session("first_page_district_index"),
        key="first_page_district", on_change=se.first_page_district_changed
    )

    payload["gereksinimler"] = st.multiselect(
        'Neye İhtiyacınız Var?',
        ['Göçük Altındayım', 'İlaç', 'Malzeme ulaşımı', 'Hastane', 'Konaklama', 'Elektrik', 'Yemek', 'Erzak',
         'Deprem alanıdan ayrılma',
         'Yardim tırı', 'Barınma', 'Yakıt', 'Ulaşım', 'Pet nakil', 'İş makinesi operatörü', 'Vinç operatörü',
         'Araç yardımı', 'Giyim', 'Diğer'],
        ['Göçük Altındayım'])

    payload["adres"] = st.text_area(
        label="Adres [ZORUNLU]", key='first_page_address', on_change=se.first_page_address_changed
    )

    st.checkbox(label="Adresi benim için otomatik doldur", key="first_page_is_address_autofill", value=True)

    payload["telefon"] = st.text_input(
        label="Telefon numarası [OPSİYONEL]"
    )

    payload["not"] = st.text_area(
        label="NOT [OPSİYONEL]"
    )
    st.button("Gönder", key="first_page_submit_button", on_click=se.first_page_on_submit_button_click, args=(payload,))

    if session_helper.get_session("first_page_is_success"):
        st.success('Mesajınız alındı!', icon="✅")
    if session_helper.get_session("first_page_is_error"):
        st.error(session_helper.get_session("first_page_is_error_message"), icon="🚨")


first_page()
