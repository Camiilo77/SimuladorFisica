import streamlit as st
from src.emsim.core.parallel_plates import solve_parallel_plates
from src.emsim.plot_utils import plot_parallel_plates

def main():
        # --------------------------
    # Estilos CSS personalizados
    # --------------------------
    st.markdown("""
    <style>

        /* ================================
           SIDEBAR OSCURO + TEXTO LEGIBLE
           ================================ */
        section[data-testid="stSidebar"] {
            background-color: #0E1117;
            border-right: 1px solid #333333;
        }

        section[data-testid="stSidebar"] * {
            color: #DCE3EB !important;
            font-size: 0.95rem;
        }

        /* ================================
           CONTENEDOR PRINCIPAL
           ================================ */
        .block-container {
            padding-top: 2rem;
        }

        /* ================================
           MÉTRICAS OSCURAS
           ================================ */
        div[data-testid="metric-container"] {
            background: #1A1D23;
            border: 1px solid #2A2D33;
            padding: 14px;
            border-radius: 12px;
            margin-bottom: 12px;
        }

        div[data-testid="metric-container"] label {
            color: #E0E6ED !important;
        }

        div[data-testid="metric-container"] span {
            color: #B5C4D1 !important;
        }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("## 🧪 Capacitor de placas paralelas (vacío)")
    st.markdown("Introduce los datos conocidos y deja en cero los que deseas calcular.")

    # Sidebar
    st.sidebar.markdown("## ⚙️ Parámetros del sistema")

    with st.sidebar.expander("📐 Geometría"):
        area = st.number_input("Área (m²)", min_value=0.0, value=0.0) or None
        distance = st.number_input("Distancia (m)", min_value=0.0, value=0.0) or None

    with st.sidebar.expander("⚡ Parámetros eléctricos"):
        capacitance = st.number_input("Capacitancia (F)", min_value=0.0, value=0.0) or None
        voltage = st.number_input("Voltaje (V)", min_value=0.0, value=0.0) or None
        charge = st.number_input("Carga (C)", min_value=0.0, value=0.0) or None

    # Replace zeros
    for x in ["area", "distance", "capacitance", "voltage", "charge"]:
        if locals()[x] == 0.0:
            locals()[x] = None

    # Compute
    result = solve_parallel_plates(area, distance, capacitance, voltage, charge)

    st.markdown("## 🧮 Resultados")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Área (m²)", f"{result['area']:.5f}" if result['area'] else "—")
        st.metric("Distancia (m)", f"{result['distance']:.5f}" if result['distance'] else "—")
        st.metric("Voltaje (V)", f"{result['voltage']:.5f}" if result['voltage'] else "—")

    with col2:
        st.metric("Capacitancia (F)", f"{result['capacitance']:.5e}" if result['capacitance'] else "—")
        st.metric("Carga (C)", f"{result['charge']:.5e}" if result['charge'] else "—")
        st.metric("Campo E (N/C)", f"{result['field']:.3e}" if result['field'] else "—")

    # Visualization
    st.markdown("## 📊 Visualización")
    fig = plot_parallel_plates(
        area_m2 = result['area'] or 0.01,
        distance_m = result['distance'] or 0.01,
        voltage_V = result['voltage'] or 1,
        field_NC = result['field'] or 1e3
    )
    st.plotly_chart(fig, use_container_width=True)
