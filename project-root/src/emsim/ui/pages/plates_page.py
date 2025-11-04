import streamlit as st
from emsim.core.parallel_plates import capacitance_parallel_plates, electric_field_parallel_plates, potential_parallel_plates, latex_deduction
from emsim.ui.controls import plates_controls
from emsim.plot_utils import plot_parallel_plates

def main():
    st.markdown("## Capacitancia en Placas Paralelas")
    st.markdown("### Deducción y fórmula")
    st.latex(latex_deduction())

    # Inputs
    area, distance, epsilon_r, voltaje, carga_in = plates_controls()

    # Cálculo físico
    C = capacitance_parallel_plates(area, distance, epsilon_r)
    V = voltaje
    if carga_in == 0 and C:
        Q = C * V
    else:
        Q = carga_in
        if C and Q > 0:
            V = potential_parallel_plates(Q, C)

    E = electric_field_parallel_plates(V, distance) if V and distance else None

    # Resultados
    st.markdown("### Resultados físicos")
    if C:
        st.write(f"**Capacitancia:** {C:.3e} F")
        st.write(f"**Carga almacenada:** {Q:.3e} C")
        st.write(f"**Diferencia de potencial:** {V:.3e} V")
        if E:
            st.write(f"**Campo eléctrico ideal:** {E:.3e} N/C")
    else:
        st.error("Verifica que todos los parámetros físicos sean positivos y razonables.")

    # Gráfico
    st.markdown("### Visualización geométrica y campo")
    fig = plot_parallel_plates(area, distance, V, E)
    st.plotly_chart(fig, use_container_width=True)
