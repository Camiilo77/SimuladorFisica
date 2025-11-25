import streamlit as st
from src.emsim.core.parallel_plates import solve_parallel_plates
from src.emsim.plot_utils import plot_parallel_plates

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
        
        /* Cambiar borde de las cajas de input */
        div.stTextInput > div > input,
        div.stNumberInput > div > input {
            border: 2px solid #FFA500;  /* marco naranja */
            border-radius: 6px;
            padding: 6px;
}

    </style>
    """, unsafe_allow_html=True)

    # ============================================
    # Título principal
    # ============================================
    st.markdown("## 🧪 Capacitor de placas paralelas (vacío)")
    st.markdown("Introduce los datos conocidos y deja vacío los que quieres calcular.")

    # ============================================
    # Sidebar organizada
    # ============================================
    st.sidebar.markdown("## ⚙️ Parámetros del sistema")

    # ---------- Grupo: Geometría ----------
    with st.sidebar.expander("📐 Geometría"):
        area = float_input("Área (m²)", default="", help="Ej: 0.01, 2e-4")
        distance = float_input("Distancia entre placas (m)", default="", help="Ej: 0.001, 5e-3")

    # ---------- Grupo: Electricidad ----------
    with st.sidebar.expander("⚡ Parámetros eléctricos"):
        capacitance = float_input("Capacitancia (F)", default="", help="Ej: 1e-12")
        voltage = float_input("Voltaje (V)", default="")
        charge = float_input("Carga (C)", default="", help="Ej: 1e-6")

    # ============================================
    # Cálculo automático
    # ============================================
    result = solve_parallel_plates(
        area=area,
        distance=distance,
        capacitance=capacitance,
        voltage=voltage,
        charge=charge
    )

    st.markdown("## 🧮 Resultados automáticos")
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Área (m²)", f"{result['area']:.5f}" if result['area'] else "—")
        st.metric("Distancia (m)", f"{result['distance']:.5f}" if result['distance'] else "—")
        st.metric("Voltaje (V)", f"{result['voltage']:.5f}" if result['voltage'] else "—")

    with col2:
        st.metric("Capacitancia (F)", f"{result['capacitance']:.5e}" if result['capacitance'] else "—")
        st.metric("Carga (C)", f"{result['charge']:.5e}" if result['charge'] else "—")
        st.metric("Campo E (N/C)", f"{result['field']:.3e}" if result['field'] else "—")

    # ============================================
    # Visualización
    # ============================================
    st.markdown("## 📊 Visualización del capacitor")
    fig = plot_parallel_plates(
        area_m2=result['area'] if (result['area'] and result['area'] > 0) else 0.01,
        distance_m=result['distance'] if (result['distance'] and result['distance'] > 0) else 0.01,
        voltage_V=result['voltage'] if (result['voltage'] and result['voltage'] > 0) else 1,
        field_NC=result['field'] if (result['field'] and result['field'] > 0) else 1e3
    )
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
