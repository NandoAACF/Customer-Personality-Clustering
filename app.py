import streamlit as st
from page_cluster import show_cluster

page = st.sidebar.selectbox("Choose Option", ("Cluster", "Model Information"))

if page == 'Cluster':
    show_cluster()
# elif page == 'Model Information':
#     show_model()