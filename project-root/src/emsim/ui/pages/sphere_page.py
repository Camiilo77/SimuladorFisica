import streamlit as st
from emsim.core.sphere import solve_sphere
from emsim.plot_utils import plot_sphere

def main():
    st.markdown("## Esfera conductora (vacío)")
    st.markdown("Completa el dato que tienes, deja en cero los que quieres calcular. Siempre verás la figura, aunque esté en ceros.")

    radius = st.sidebar.number_input("Radio de la esfera (m)", min_value=0.0, value=0.0, step=0.0001, format="%.5f") or None
    capacitance = st.sidebar.number_input("Capacitancia (F)", min_value=0.0, value=0.0, step=1e-12, format="%.5e") or None
    voltage = st.sidebar.number_input("Voltaje (V)", min_value=0.0, value=0.0, step=0.01, format="%.2f") or None
    charge = st.sidebar.number_input("Carga (C)", min_value=0.0, value=0.0, step=1e-12, format="%.5e") or None
    area = st.sidebar.number_input("Área superficial (m²)", min_value=0.0, value=0.0, step=0.001, format="%.5f") or None

    if radius == 0.0: radius = None
    if capacitance == 0.0: capacitance = None
    if voltage == 0.0: voltage = None
    if charge == 0.0: charge = None
    if area == 0.0: area = None

    result = solve_sphere(radius=radius, capacitance=capacitance, charge=charge, voltage=voltage, area=area)
    st.markdown("### Resultados automáticos")
    st.write(f"**Radio**: {result['radius']:.5f} m" if result['radius'] else "Radio no definido")
    st.write(f"**Capacitancia**: {result['capacitance']:.5e} F" if result['capacitance'] else "Capacitancia no definida")
    st.write(f"**Voltaje**: {result['voltage']:.5f} V" if result['voltage'] else "Voltaje no definido")
    st.write(f"**Carga**: {result['charge']:.5e} C" if result['charge'] else "Carga no definida")
    st.write(f"**Área superficial**: {result['area']:.5f} m²" if result['area'] else "Área no definida")

    # Figura: si no hay radio calculado, usa valor estándar
    fig = plot_sphere(
        radius_m = result['radius'] if (result['radius'] and result['radius'] > 0) else 0.05,
        charge = result['charge']
    )
    st.plotly_chart(fig, use_container_width=True)
