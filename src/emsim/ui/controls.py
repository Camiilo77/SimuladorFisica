import streamlit as st

def plates_controls():
    """
    Controles Streamlit para placas paralelas.
    Devuelve: (área, distancia, epsilon_r, voltaje, carga)
    """
    st.sidebar.subheader("Parámetros físicos")
    area = st.sidebar.number_input(
        "Área de cada placa [m²]",
        min_value=0.00001,    # Permite valores muy pequeños (10 µm²)
        value=0.01,           # Ejemplo default: 10cm x 10cm
        step=0.00001,         # Paso mínimo
        format="%.5f",        # Mostrar hasta 5 decimales
        help="Área superficial efectiva de las placas (ej: 0.01 = 10cm x 10cm)"
    )
    distance = st.sidebar.number_input(
        "Distancia entre placas [m]",
        min_value=0.00001,    # Permite valores de hasta 10 µm
        value=0.01,
        step=0.00001,
        format="%.5f",
        help="Separación uniforme entre placas"
    )
    epsilon_r = st.sidebar.number_input(
        "Permitividad relativa (εᵣ)",
        min_value=1.85e-12,
        value=8.85e-12,            
        step=0.01,
        format="%.2f",
        help="Aire=1.00, papel≈3, vidrio≈5~10, etc."
    )
    voltaje = st.sidebar.number_input(
        "Voltaje aplicado [V]",
        min_value=0.0,
        value=5.0,
        step=0.01,
        format="%.2f",
        help="Diferencia de potencial entre placas"
    )
    carga = st.sidebar.number_input(
        "Carga en placas [C]",
        min_value=0.0,
        value=0.0,
        step=1e-9,
        format="%.2e",
        help="Si dejas en 0, se usará Q = C·V calculado automáticamente."
    )
    return area, distance, epsilon_r, voltaje, carga
