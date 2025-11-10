import streamlit as st
from emsim.core.parallel_plates import solve_parallel_plates
from emsim.plot_utils import plot_parallel_plates

def main():
    st.markdown("## Capacitor de placas paralelas (vacío)")
    st.markdown("Completa los datos que conozcas y deja vacío el que quieres que se calcule (pon 0 o deja en blanco):")

    # Entradas (puedes ajustar los min_value)
    area = st.sidebar.number_input(
        "Área de placa (m²) [0 si quieres calcular]", min_value=0.0, value=0.0,
        step=0.001, format="%.5f"
    ) or None
    separation = st.sidebar.number_input(
        "Distancia entre placas (m) [0 si quieres calcular]", min_value=0.0, value=0.0,
        step=0.0001, format="%.5f"
    ) or None
    capacitance = st.sidebar.number_input(
        "Capacitancia (F) [0 si quieres calcular]", min_value=-90000.0, value=0.0,
        step=1e-12, format="%.5e"
    ) or None
    voltage = st.sidebar.number_input(
        "Voltaje (V) [0 si quieres calcular]", min_value=-90000.0, value=0.0,
        step=0.01, format="%.2f"
    ) or None
    charge = st.sidebar.number_input(
        "Carga (C) [0 si quieres calcular]", min_value=-9000.0, value=0.0,
        step=1e-12, format="%.5e"
    ) or None

    # Si el usuario deja en cero o None, la función lo calcula
    if area == 0.0:
        area = None
    if separation == 0.0:
        separation = None
    if capacitance == 0.0:
        capacitance = None
    if voltage == 0.0:
        voltage = None
    if charge == 0.0:
        charge = None

    st.markdown("### Resultados automáticos")
    result = solve_parallel_plates(area=area, distance=separation, capacitance=capacitance, voltage=voltage, charge=charge)
    st.write(f"**Área de placa**: {result['area']:.5f} m²" if result['area'] else "Área no definida")
    st.write(f"**Distancia entre placas**: {result['distance']:.5f} m" if result['distance'] else "Distancia no definida")
    st.write(f"**Capacitancia**: {result['capacitance']:.5e} F" if result['capacitance'] else "Capacitancia no definida")
    st.write(f"**Voltaje**: {result['voltage']:.5f} V" if result['voltage'] else "Voltaje no definido")
    st.write(f"**Carga**: {result['charge']:.5e} C" if result['charge'] else "Carga no definida")
    st.write(f"**Campo eléctrico ideal**: {result['field']:.3e} N/C" if result['field'] else "Campo E no definido")

    # Gráfica
    fig = plot_parallel_plates(
        area_m2 = result['area'] or 0.01,
        distance_m = result['distance'] or 0.01,
        voltage_V = result['voltage'] or 1,
        field_NC = result['field'] or 1e3
    )
    st.plotly_chart(fig, use_container_width=True)
