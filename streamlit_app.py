from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import extra_streamlit_components as stx





import datetime
st.write("# Cookie Manager")


def get_manager():
    return stx.CookieManager()

cookie_manager = get_manager()

st.subheader("All Cookies:")
cookies = cookie_manager.get_all()
st.write(cookies)

c1, c2, c3 = st.columns(3)

with c1:
    st.subheader("Get Cookie:")
    cookie = st.text_input("Cookie", key="0")
    clicked = st.button("Get")
    if clicked:
        value = cookie_manager.get(cookie=cookie)
        st.write(value)
with c2:
    st.subheader("Set Cookie:")
    cookie = st.text_input("Cookie", key="1")
    val = st.text_input("Value")
    if st.button("Add"):
        cookie_manager.set(cookie, val, expires_at=datetime.datetime(year=2022, month=2, day=2))

        
        
with c3:
    st.subheader("Delete Cookie:")
    cookie = st.text_input("Cookie", key="2")
    if st.button("Delete"):
        cookie_manager.delete(cookie)
