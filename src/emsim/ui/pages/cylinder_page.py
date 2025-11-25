import streamlit as st
from src.emsim.core.cylinder import solve_coaxial_cylinder
from src.emsim.plot_utils import plot_cylinder

# ============================================
# Función para permitir negativos y notación científica
# ============================================
def float_input(label, default=None, help=None):
    raw = st.text_input(label, value=str(default) if default is not None else "", help=help)
    try:
        return float(raw)
    except:
        if raw.strip() != "":
            st.warning(f"Valor no válido en '{label}'. Usa números, negativos o notación científica (ej: 1e-6).")
        return None


def main():

    # ============================================
    # Estilos CSS personalizados
    # ============================================
    st.markdown("""
    <style>

        section[data-testid="stSidebar"] {
            background-color: #0E1117;
            border-right: 1px solid #333333;
        }

        section[data-testid="stSidebar"] * {
            color: #DCE3EB !important;
            font-size: 0.95rem;
        }

        .block-container {
            padding-top: 2rem;
        }

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

    # ============================================
    # Título principal
    # ============================================
    st.markdown("## 📡 Cilindro coaxial (vacío)")
    st.markdown("Introduce los datos conocidos y deja vacío los que quieres calcular.")

    # ============================================
    # Sidebar organizada
    # ============================================
    st.sidebar.markdown("## ⚙️ Parámetros del sistema")

    # ---------- Grupo: Geometría ----------
    with st.sidebar.expander("📐 Geometría"):
        length = float_input("Longitud (m)", default="", help="Ej: 0.1, 2e-3, -0.05")
        r_in = float_input("Radio interior (m)", default="")
        r_out = float_input("Radio exterior (m)", default="")

    # ---------- Grupo: Electricidad ----------
    with st.sidebar.expander("⚡ Parámetros eléctricos"):
        capacitance = float_input("Capacitancia (F)", default="", help="Ej: 3e-12")
        voltage = float_input("Voltaje (V)", default="")
        charge = float_input("Carga (C)", default="", help="Ej: 1e-6")

    # ---------- Grupo: Propiedades derivadas ----------
    with st.sidebar.expander("📏 Propiedades derivadas"):
        area = float_input("Área (m²)", default="")
        volume = float_input("Volumen (m³)", default="")

    # ============================================
    # Cálculo automático
    # ============================================
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

    col1, col2 = st.columns(2)

    # ---------- Métricas ----------
    with col1:
        st.metric("Longitud (m)", f"{result['length']:.5f}" if result['length'] else "—")
        st.metric("Radio interior (m)", f"{result['r_in']:.5f}" if result['r_in'] else "—")
        st.metric("Capacitancia (F)", f"{result['capacitance']:.5e}" if result['capacitance'] else "—")
        st.metric("Área interna (m²)", f"{result['area']:.5f}" if result['area'] else "—")

    with col2:
        st.metric("Radio exterior (m)", f"{result['r_out']:.5f}" if result['r_out'] else "—")
        st.metric("Voltaje (V)", f"{result['voltaje']:.5f}" if result['voltaje'] else "—")
        st.metric("Carga (C)", f"{result['charge']:.5e}" if result['charge'] else "—")
        st.metric("Volumen interno (m³)", f"{result['volume']:.6f}" if result['volume'] else "—")

    # ============================================
    # Visualización
    # ============================================
    st.markdown("## 📊 Visualización del cilindro")

    fig = plot_cylinder(
        length_m=result['length'] if (result['length'] and result['length'] > 0) else 0.1,
        r_in_m=result['r_in'] if (result['r_in'] and result['r_in'] > 0) else 0.01,
        r_out_m=result['r_out'] if (result['r_out'] and result['r_out'] > 0) else 0.02,
    )

    st.plotly_chart(fig, use_container_width=True)
