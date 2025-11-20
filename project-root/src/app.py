import sys
import os

# ============================
#  AÑADIR /src AL PYTHONPATH
# ============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # ruta: /src
sys.path.append(BASE_DIR)

import streamlit as st
from emsim.ui.pages.plates_page import main as plates_page
from emsim.ui.pages.sphere_page import main as sphere_page
from emsim.ui.pages.cylinder_page import main as cylinder_page


PAGES = {
    "Placas Paralelas": plates_page,
    "Esfera Conductora": sphere_page,
    "Cilindro/Coaxial": cylinder_page,
}

st.set_page_config(page_title="Simulador de Capacitancia", page_icon="🧲")
st.sidebar.title("Navegación")
choice = st.sidebar.radio("Selecciona la geometría:", list(PAGES.keys()))
PAGES[choice]()
