from helpers.streamlit_helpers import streamlit_helper as sh, streamlit_events as se, \
    streamlit_session_helper as session_helper
import streamlit as st
from streamlit_folium import st_folium
from dotenv import load_dotenv
from models import GLOBALS

load_dotenv()

payload = {}


def InitComponents():
    sh.SetInitialStreamlitStates(sections=["global", "first_page"])
    st.set_page_config(layout="wide")


InitComponents()


def first_page():
    st.header("Yardım Çağrısında Bulun!")
    st.warning(
        "Mobilden veya küçük çözünürlüklü cihazlardan giriyorsanız sol üstteki oka '>' basıp menüye ulaşabilirsiniz!")
    st.info("Bu sayfada destek bildiriminde bulunabilir ve yurttaşlarımıza umut olabilirsiniz!")

    # folium_static(fig=session_helper.get_session("first_page_map"), width=1400, height=600)

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
        GLOBALS.NEEDS,
        GLOBALS.NEEDS[0])

    payload["adres"] = st.text_area(
        label="Adres [ZORUNLU]", key='first_page_address', on_change=se.first_page_address_changed
    )

    st.checkbox(label="Adresi benim için otomatik doldur", key="first_page_is_address_autofill", value=False)

    payload["isim"] = st.text_input(
        label="İsim [ZORUNLU]"
    )

    payload["telefon"] = st.text_input(
        label="Telefon numarası [OPSİYONEL]"
    )

    payload["notlar"] = st.text_area(
        label="NOT [OPSİYONEL]"
    )

    with st.expander("Girdiğiniz Konumu Haritada Görüntüleyin:"):
        st_folium(fig=session_helper.get_session("first_page_map"), height=400)  # , width=1400, height=600)

    st.button("Gönder", key="first_page_submit_button", on_click=se.first_page_on_submit_button_click,
              args=(payload,))

    if session_helper.get_session("first_page_is_success"):
        st.success('Mesajınız alındı!', icon="✅")
    if session_helper.get_session("first_page_is_error"):
        st.error(session_helper.get_session("first_page_error_message"), icon="🚨")



