import streamlit as st

def show_information():
    st.title('Cluster Information')

    st.write('**Model:** KMeans Clustering')

    st.write('**Karakteristik Cluster 0:**')
    st.write('- Income menengah bawah (25000-50000)')
    st.write('- Hemat dalam berbelanja')
    st.write('- Mayoritas memiliki anak')
    st.write('- Jarang membeli barang via katalog')

    st.write('**Karakteristik Cluster 1:**')
    st.write('- Income menengah atas (50000-75000)')
    st.write('- Lebih boros dalam berbelanja')
    st.write('- Suka membeli wine')

    st.write('**Karakteristik Cluster 2:**')
    st.write('- Income rendah (< 25000)')
    st.write('- Jarang berbelanja')
    st.write('- Orang berusia lebih muda')
    st.write('- Hampir tidak pernah membeli daging')
    st.write('- Membeli barang ketika ada diskon')

    st.write('**Karakteristik Cluster 3:**')
    st.write('- Income tinggi (> 75000)')
    st.write('- Mengeluarkan paling banyak uang ketika berbelanja')
    st.write('- Mayoritas tidak memiliki anak')
    st.write('- Suka membeli berbagai macam variasi produk')
    st.write('- Tidak menunggu diskon untuk membeli barang')