from helpers.streamlit_helpers import streamlit_helper as sh, streamlit_events as se, \
    streamlit_session_helper as session_helper
import streamlit as st
from streamlit_folium import folium_static
from models import GLOBALS
from services import redis_service, record_service


def InitComponents():
    sh.SetInitialStreamlitStates(sections=["global", "second_page"])


def second_page():
    InitComponents()

    folium_static(fig=session_helper.get_session("second_page_map"))

    st.sidebar.selectbox(
        label="İl", options=session_helper.get_session("province_list"), key="second_page_province",
        on_change=se.second_page_province_changed, index=session_helper.get_session("second_page_province_index"),
    )

    st.sidebar.selectbox(
        label="İlçe", options=session_helper.get_session("second_page_selectable_districts"),
        index=session_helper.get_session("second_page_district_index"),
        key="second_page_district", on_change=se.second_page_district_changed
    )
    st.sidebar.text_input(label="İsim", key="second_page_name")

    st.sidebar.multiselect(
        'Neye İhtiyacınız Var?',
        GLOBALS.NEEDS,
        GLOBALS.NEEDS[0], key="second_page_needs")

    st.sidebar.text_area("Telefon", key="second_page_phone")
    st.sidebar.text_area("Not", key="second_page_notes")

    col1, col2 = st.sidebar.columns(2)

    with col1:
        st.date_input(label="Başlangıç Tarihi", key="second_page_start_date_filter",
                      on_change=se.second_page_start_date_filter_changed,
                      value=st.session_state.second_page_start_date_value)
    with col2:
        st.date_input(label="Bitiş Tarihi", key="second_page_end_date_filter",
                      on_change=se.second_page_end_date_filter_changed,
                      value=st.session_state.second_page_end_date_value)

    col4, col5, col6 = st.sidebar.columns(3, gap="small")
    with col4:
        st.button("Filtrele", key="second_page_filter_button", on_click=se.second_page_filter_click)
    with col5:
        st.button("Filtreyi Temizle", key="second_page_clear_filter_button", on_click=se.second_page_refresh_click)
    with col6:
        st.button("Yenile", key="second_page_refresh_button", on_click=se.second_page_refresh_click)

    for rec in sh.GetCallRecordsDetails():
        st.code(rec, language="markdown")

    total_page_count = st.session_state.second_page_last_call_record_count / GLOBALS.PAGE_SIZE
    cols = st.columns(int(total_page_count) + 1)

    for i in range(int(total_page_count) + 1):
        cols[i].button(str(i + 1), on_click=se.second_page_pager_button_click, args=(i,))


second_page()
