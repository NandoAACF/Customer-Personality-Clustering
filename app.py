import streamlit as st
from page_cluster import show_cluster
from page_information import show_information
from page_visualisasi import show_visualisasi
from page_insight_for_perusahaan import show_insight_perusahaan

page = st.sidebar.selectbox("Choose Option", ("Cluster", "Information", "Visualisasi", "Insight untuk Perusahaan"))

if page == 'Cluster':
    show_cluster()
elif page == 'Information':
    show_information()
elif page == 'Visualisasi':
    show_visualisasi()
elif page == 'Insight untuk Perusahaan':
    show_insight_perusahaan()