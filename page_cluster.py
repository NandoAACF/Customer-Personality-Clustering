import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('models/kmeans.pickle', 'rb') as f:
        model = pickle.load(f)
    return model

model = load_model()

def show_cluster():
    st.title('Customer Personality Clustering')