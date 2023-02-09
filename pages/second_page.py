from helpers.streamlit_helpers import streamlit_helper as sh, streamlit_events as se, \
    streamlit_session_helper as session_helper
import streamlit as st
from streamlit_folium import folium_static
from services import redis_service


def InitComponents():
    sh.SetInitialStreamlitStates(sections=["global", "second_page"])


def second_page():
    InitComponents()

    st.selectbox(
        label="İl [ZORUNLU]", options=session_helper.get_session("province_list"), key="second_page_province",
        on_change=se.second_page_province_changed, index=session_helper.get_session("second_page_province_index"),
    )

    st.selectbox(
        label="İlçe [ZORUNLU]", options=session_helper.get_session("second_page_selectable_districts"),
        index=session_helper.get_session("second_page_district_index"),
        key="second_page_district", on_change=se.second_page_district_changed
    )
    # Sayfalar arası iller gelmiyor
    st.multiselect(
        'Neye İhtiyacınız Var?',
        ['Göçük Altındayım', 'İlaç', 'Malzeme ulaşımı', 'Hastane', 'Konaklama', 'Elektrik', 'Yemek', 'Erzak',
         'Deprem alanıdan ayrılma',
         'Yardim tırı', 'Barınma', 'Yakıt', 'Ulaşım', 'Pet nakil', 'İş makinesi operatörü', 'Vinç operatörü',
         'Araç yardımı', 'Giyim', 'Diğer'],
        ['Göçük Altındayım'], key="second_page_needs")


# Cacheteki ilk kaydın tarihini al Vusala gönder yenilemek için gelen verileri cahceteki datanın başıan ekle prepend yap

# st.markdown("Welcome!")

# folium_static(fig=session_helper.get_session("first_page_map"))


second_page()
