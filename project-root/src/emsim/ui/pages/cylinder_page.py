import streamlit as st
from emsim.core.cylinder import solve_coaxial_cylinder
from emsim.plot_utils import plot_cylinder

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

    # --------------------------
    # Título principal
    # --------------------------
    st.markdown("## 📡 Cilindro coaxial (vacío)")
    st.markdown("Introduce los datos conocidos y deja en cero los que quieres calcular.")

    # --------------------------
    # Sidebar organizada
    # --------------------------
    st.sidebar.markdown("## ⚙️ Parámetros del sistema")

    # Grupo 1: Geometría
    with st.sidebar.expander("📐 Geometría"):
        length = st.number_input("Longitud (m)", min_value=0.0, value=0.0, step=0.001, format="%.5f") or None
        r_in = st.number_input("Radio interior (m)", min_value=0.0, value=0.0, step=0.0001, format="%.5f") or None
        r_out = st.number_input("Radio exterior (m)", min_value=0.0, value=0.0, step=0.0001, format="%.5f") or None

    # Grupo 2: Electricidad
    with st.sidebar.expander("⚡ Parámetros eléctricos"):
        capacitance = st.number_input("Capacitancia (F)", min_value=0.0, value=0.0, step=1e-12, format="%.5e") or None
        voltage = st.number_input("Voltaje (V)", min_value=0.0, value=0.0, step=0.01, format="%.2f") or None
        charge = st.number_input("Carga (C)", min_value=0.0, value=0.0, step=1e-12, format="%.5e") or None

    # Grupo 3: Propiedades derivadas
    with st.sidebar.expander("📏 Propiedades derivadas"):
        area = st.number_input("Área  (m²)", min_value=0.0, value=0.0, step=0.001, format="%.5f") or None
        volume = st.number_input("Volumen  (m³)", min_value=0.0, value=0.0, step=1e-6, format="%.6f") or None

    # Reemplazar ceros por None
    for var_name in ["length", "r_in", "r_out", "capacitance", "voltage", "charge", "area", "volume"]:
        if locals()[var_name] == 0.0:
            locals()[var_name] = None

    # --------------------------
    # Cálculo automático
    # --------------------------
    result = solve_coaxial_cylinder(
        length=length,
        r_in=r_in,
        r_out=r_out,
        capacitance=capacitance,
        charge=charge,
        voltage=voltage,
        area=area,
        volume=volume
    )

    st.markdown("## 🧮 Resultados automáticos")

    # Métricas
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Longitud (m)", f"{result['length']:.5f}" if result['length'] else "—")
        st.metric("Radio interior (m)", f"{result['r_in']:.5f}" if result['r_in'] else "—")
        st.metric("Capacitancia (F)", f"{result['capacitance']:.5e}" if result['capacitance'] else "—")
        st.metric("Área interna (m²)", f"{result['area']:.5f}" if result['area'] else "—")

    with col2:
        st.metric("Radio exterior (m)", f"{result['r_out']:.5f}" if result['r_out'] else "—")
        st.metric("Voltaje (V)", f"{result['voltage']:.5f}" if result['voltage'] else "—")
        st.metric("Carga (C)", f"{result['charge']:.5e}" if result['charge'] else "—")
        st.metric("Volumen interno (m³)", f"{result['volume']:.6f}" if result['volume'] else "—")

    # --------------------------
    # Visualización
    # --------------------------
    st.markdown("## 📊 Visualización del cilindro")

    fig = plot_cylinder(
        length_m = result['length'] if (result['length'] and result['length'] > 0) else 0.1,
        r_in_m = result['r_in'] if (result['r_in'] and result['r_in'] > 0) else 0.01,
        r_out_m = result['r_out'] if (result['r_out'] and result['r_out'] > 0) else 0.02
    )

    st.plotly_chart(fig, use_container_width=True)
