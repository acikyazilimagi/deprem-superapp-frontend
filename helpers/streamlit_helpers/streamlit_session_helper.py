import streamlit as st


def set_session(key, value):
    st.session_state[key] = value


def get_session(key):
    return st.session_state[key]
