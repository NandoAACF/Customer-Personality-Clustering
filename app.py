import streamlit as st
from page_cluster import show_cluster
from page_information import show_information

page = st.sidebar.selectbox("Choose Option", ("Cluster", "Information"))

if page == 'Cluster':
    show_cluster()
elif page == 'Information':
    show_information()