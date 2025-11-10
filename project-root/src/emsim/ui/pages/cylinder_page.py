import streamlit as st
from emsim.core.cylinder import solve_coaxial_cylinder
from emsim.plot_utils import plot_cylinder

def main():
    st.markdown("## Cilindro coaxial (vacío)")
    st.markdown("Completa los datos conocidos, deja en cero los que quieres calcular. Siempre tendrás la figura visible.")

    length = st.sidebar.number_input("Longitud (m)", min_value=0.0, value=0.0, step=0.001, format="%.5f") or None
    r_in = st.sidebar.number_input("Radio interior (m)", min_value=0.0, value=0.0, step=0.0001, format="%.5f") or None
    r_out = st.sidebar.number_input("Radio exterior (m)", min_value=0.0, value=0.0, step=0.0001, format="%.5f") or None
    capacitance = st.sidebar.number_input("Capacitancia (F)", min_value=0.0, value=0.0, step=1e-12, format="%.5e") or None
    voltage = st.sidebar.number_input("Voltaje (V)", min_value=0.0, value=0.0, step=0.01, format="%.2f") or None
    charge = st.sidebar.number_input("Carga (C)", min_value=0.0, value=0.0, step=1e-12, format="%.5e") or None
    area = st.sidebar.number_input("Área lateral interna (m²)", min_value=0.0, value=0.0, step=0.001, format="%.5f") or None
    volume = st.sidebar.number_input("Volumen interno (m³)", min_value=0.0, value=0.0, step=1e-6, format="%.6f") or None

    if length == 0.0: length = None
    if r_in == 0.0: r_in = None
    if r_out == 0.0: r_out = None
    if capacitance == 0.0: capacitance = None
    if voltage == 0.0: voltage = None
    if charge == 0.0: charge = None
    if area == 0.0: area = None
    if volume == 0.0: volume = None

    result = solve_coaxial_cylinder(length=length, r_in=r_in, r_out=r_out, capacitance=capacitance,
                                    charge=charge, voltage=voltage, area=area, volume=volume)
    st.markdown("### Resultados automáticos")
    st.write(f"**Longitud**: {result['length']:.5f} m" if result['length'] else "Longitud no definida")
    st.write(f"**Radio interior**: {result['r_in']:.5f} m" if result['r_in'] else "radio interior no definido")
    st.write(f"**Radio exterior**: {result['r_out']:.5f} m" if result['r_out'] else "radio exterior no definido")
    st.write(f"**Capacitancia**: {result['capacitance']:.5e} F" if result['capacitance'] else "Capacitancia no definida")
    st.write(f"**Voltaje**: {result['voltage']:.5f} V" if result['voltage'] else "Voltaje no definido")
    st.write(f"**Carga**: {result['charge']:.5e} C" if result['charge'] else "Carga no definida")
    st.write(f"**Área interna lateral**: {result['area']:.5f} m²" if result['area'] else "Área no definida")
    st.write(f"**Volumen interno**: {result['volume']:.6f} m³" if result['volume'] else "Volumen no definido")

    # Figura: valores estándar si no hay input físico válido
    fig = plot_cylinder(
        length_m = result['length'] if (result['length'] and result['length'] > 0) else 0.1,
        r_in_m = result['r_in'] if (result['r_in'] and result['r_in'] > 0) else 0.01,
        r_out_m = result['r_out'] if (result['r_out'] and result['r_out'] > 0 and result['r_out'] > result['r_in']) else 0.02
    )
    st.plotly_chart(fig, use_container_width=True)
