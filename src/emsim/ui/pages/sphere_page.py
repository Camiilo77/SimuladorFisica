import streamlit as st
from src.emsim.core.sphere import solve_sphere
from src.emsim.plot_utils import plot_sphere

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

        /* ================================
           Sidebar oscuro y texto legible
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
           Contenedor principal
           ================================ */
        .block-container {
            padding-top: 2rem;
        }

        /* ================================
           Métricas oscuras
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

        /* ================================
           Inputs con fondo diferenciado y borde color
           ================================ */
        div.stTextInput > div > input,
        div.stNumberInput > div > input {
            background-color: #1E1E2E !important;  /* fondo oscuro, distinto al sidebar */
            color: #FFFFFF !important;             /* texto blanco */
            border: 2px solid #FFA500 !important;  /* borde naranja */
            border-radius: 6px !important;
            padding: 6px !important;
        }

    </style>
    """, unsafe_allow_html=True)

    # ============================================
    # Título principal
    # ============================================
    st.markdown("## ⚪ Esfera conductora (vacío)")
    st.markdown("Completa los datos conocidos y deja vacío los que deseas calcular.")

    # ============================================
    # Sidebar organizada
    # ============================================
    st.sidebar.markdown("## ⚙️ Parámetros del sistema")

    with st.sidebar.expander("📐 Geometría"):
        radius = float_input("Radio (m)", default="", help="Ej: 0.05, 2e-2")

    with st.sidebar.expander("⚡ Parámetros eléctricos"):
        capacitance = float_input("Capacitancia (F)", default="", help="Ej: 1e-12")
        voltage = float_input("Voltaje (V)", default="")
        charge = float_input("Carga (C)", default="", help="Ej: 1e-6")
        area = float_input("Área superficial (m²)", default="", help="Ej: 0.03")

    # ============================================
    # Cálculo automático
    # ============================================
    result = solve_sphere(
        radius=radius,
        capacitance=capacitance,
        voltage=voltage,
        charge=charge,
        area=area
    )

    st.markdown("## 🧮 Resultados automáticos")
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Radio (m)", f"{result['radius']:.5f}" if result['radius'] else "—")
        st.metric("Voltaje (V)", f"{result['voltage']:.5f}" if result['voltage'] else "—")

    with col2:
        st.metric("Capacitancia (F)", f"{result['capacitance']:.5e}" if result['capacitance'] else "—")
        st.metric("Carga (C)", f"{result['charge']:.5e}" if result['charge'] else "—")
        st.metric("Área superficial (m²)", f"{result['area']:.5f}" if result['area'] else "—")

    # ============================================
    # Visualización
    # ============================================
    st.markdown("## 📊 Visualización de la esfera")
    fig = plot_sphere(
        radius_m=result['radius'] if (result['radius'] and result['radius'] > 0) else 0.05,
        charge=result['charge'] if result['charge'] else 1e-6
    )
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
