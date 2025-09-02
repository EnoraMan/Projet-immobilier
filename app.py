import os
import streamlit as st
import requests

API_URL = os.getenv("API_URL", "http://localhost:8000")  

st.title("Estimation immobilière sur la ville de Bordeaux")

surface_terrain = st.number_input("Superficie terrain", 0)
surface_bati = st.number_input("Surface m²", 0)
nb_pieces = st.number_input("Nb de pièces", 0)

if st.button("Estimer"):
    data = {
        "surface_terrain": surface_terrain,
        "surface_reelle_bati": surface_bati,
        "nombre_pieces_principales": nb_pieces,
    }
    r = requests.post(f"{API_URL}/predict", json={"data": data})
    st.write("Prix estimé :", r.json()["prediction"])
