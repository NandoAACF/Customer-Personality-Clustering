import streamlit as st
import pickle
import numpy as np

with open('models/kmeans.pickle', 'rb') as f:
    model = pickle.load(f)

def show_cluster():
    st.title('Customer Personality Clustering')

    education = st.selectbox('Education', ("Undergraduate", "Graduate", "Post Graduate"))
    if education == 'Undergraduate':
        education = 2
    elif education == 'Graduate':
        education = 0
    elif education == 'Post Graduate':
        education = 1

    marital_status = st.selectbox('Status', ("Not Single", "Single"))
    if marital_status == 'Not Single':
        marital_status = 0
    elif marital_status == 'Single':
        marital_status = 1

    income = st.number_input('Income')

    Recency = st.select_slider('Recency', options=[i for i in range(1, 100)])

    MntWines = st.number_input('Money Spent for Wine')

    MntFruits = st.number_input('Money Spent for Fruits')

    MntMeatProducts = st.number_input('Money Spent for Meat')

    MntFishProducts = st.number_input('Money Spent for Fish')

    MntSweetProducts = st.number_input('Money Spent for Sweet')

    MntGoldProds = st.number_input('Money Spent for Gold')

    NumDealsPurchases = st.number_input('Number of Purchases with Discount')

    NumWebPurchases = st.number_input('Number of Purchases via Web')

    NumCatalogPurchases = st.number_input('Number of Purchases via Catalog')

    NumStorePurchases = st.number_input('Number of Purchases via Store')

    NumWebVisitsMonth = st.number_input('Number of Visits to Web')

    days_since_last_purchase = st.number_input('Days Since Last Purchase')

    Age = st.select_slider('Age', options=[i for i in range(1, 120)])

    Total_Children = st.select_slider('Total Children', options=[i for i in range(0, 10)])

    Total_Spent = MntWines + MntFruits + MntMeatProducts + MntFishProducts + MntSweetProducts + MntGoldProds

    Total_Purchases = NumDealsPurchases + NumWebPurchases + NumCatalogPurchases + NumStorePurchases

    ok = st.button('Show Cluster')
    if ok:
        X = np.array([education, marital_status, income, Recency, MntWines, MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts, MntGoldProds, NumDealsPurchases, NumWebPurchases, NumCatalogPurchases, NumStorePurchases, NumWebVisitsMonth, days_since_last_purchase, Age, Total_Children, Total_Spent, Total_Purchases])

        cluster = model.predict([X])

        if cluster == 0:
            st.subheader('Customer Cluster: 0')
            st.write('**Karakteristik Cluster 0:**')
            st.write('- Income menengah bawah (25000-50000)')
            st.write('- Hemat dalam berbelanja')
            st.write('- Mayoritas memiliki anak')
            st.write('- Jarang membeli barang via katalog')
        elif cluster == 1:
            st.subheader('Customer Cluster: 1')
            st.write('**Karakteristik Cluster 1:**')
            st.write('- Income menengah atas (50000-75000)')
            st.write('- Lebih boros dalam berbelanja')
            st.write('- Suka membeli wine')
        elif cluster == 2:
            st.subheader('Customer Cluster: 2')
            st.write('**Karakteristik Cluster 2:**')
            st.write('- Income rendah (< 25000)')
            st.write('- Jarang berbelanja')
            st.write('- Orang berusia lebih muda')
            st.write('- Hampir tidak pernah membeli daging')
            st.write('- Membeli barang ketika ada diskon')
        elif cluster == 3:
            st.subheader('Customer Cluster: 3')
            st.write('**Karakteristik Cluster 3:**')
            st.write('- Income tinggi (> 75000)')
            st.write('- Mengeluarkan paling banyak uang ketika berbelanja')
            st.write('- Mayoritas tidak memiliki anak')
            st.write('- Suka membeli berbagai macam variasi produk')
            st.write('- Tidak menunggu diskon untuk membeli barang')
        

    