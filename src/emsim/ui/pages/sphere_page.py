import streamlit as st
from src.emsim.core.sphere import solve_sphere
from src.emsim.plot_utils import plot_sphere


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

    st.markdown("## ⚪ Esfera conductora (vacío)")
    st.markdown("Completa los datos conocidos y deja en cero los que deseas calcular.")

    st.sidebar.markdown("## ⚙️ Parámetros")

    with st.sidebar.expander("📐 Geometría"):
        radius = st.number_input("Radio (m)", min_value=0.0, value=0.0) or None

    with st.sidebar.expander("⚡ Electricidad"):
        capacitance = st.number_input("Capacitancia (F)", min_value=0.0, value=0.0) or None
        voltage = st.number_input("Voltaje (V)", min_value=0.0, value=0.0) or None
        charge = st.number_input("Carga (C)", min_value=0.0, value=0.0) or None
        area = st.number_input("Área superficial (m²)", min_value=0.0, value=0.0) or None

    for x in ["radius", "capacitance", "voltage", "charge", "area"]:
        if locals()[x] == 0.0:
            locals()[x] = None

    result = solve_sphere(radius, capacitance, charge, voltage, area)

    st.markdown("## 🧮 Resultados")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Radio (m)", f"{result['radius']:.5f}" if result['radius'] else "—")
        st.metric("Voltaje (V)", f"{result['voltage']:.5f}" if result['voltage'] else "—")

    with col2:
        st.metric("Capacitancia (F)", f"{result['capacitance']:.5e}" if result['capacitance'] else "—")
        st.metric("Carga (C)", f"{result['charge']:.5e}" if result['charge'] else "—")

    st.markdown("## 📊 Visualización")
    fig = plot_sphere(
        radius_m = result['radius'] or 0.05,
        charge = result['charge']
    )
    st.plotly_chart(fig, use_container_width=True)
