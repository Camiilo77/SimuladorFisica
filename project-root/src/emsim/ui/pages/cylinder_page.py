import streamlit as st
from emsim.core.cylinder import capacitance_coaxial_cylinder, potential_coaxial, latex_deduction
from emsim.plot_utils import plot_cylinder  # Debes crear esta función para la gráfica 3D
import numpy as np

def main():
    st.markdown("## Capacitancia de Cilindro/Coaxial")
    st.markdown("### Deducción y fórmula")
    st.latex(latex_deduction())

    st.sidebar.subheader("Parámetros físicos")
    length = st.sidebar.number_input(
        "Longitud [m]", min_value=0.0001, value=0.10,
        help="Longitud del cilindro"
    )
    radius_inner = st.sidebar.number_input(
        "Radio interior (a) [m]", min_value=0.0001, value=0.01,
        help="Radio del cilindro interno"
    )
    radius_outer = st.sidebar.number_input(
        "Radio exterior (b) [m]", min_value=radius_inner+1e-6, value=0.03,
        help="Radio del cilindro externo (b > a)"
    )
    epsilon_r = st.sidebar.number_input(
        "Permitividad relativa (εᵣ)", min_value=1.0, value=1.0,
        help="Material dieléctrico entre los cilindros"
    )
    charge = st.sidebar.number_input(
        "Carga total [C]", value=1e-9,
        help="Carga depositada entre los cilindros"
    )

    # Cálculo de capacitancia
    C = capacitance_coaxial_cylinder(length, radius_inner, radius_outer, epsilon_r)
    
    # Potencial para punto entre cilindros (r > a y r < b)
    r_eval = st.sidebar.number_input(
        "Radio para potencial [m]", min_value=radius_inner+1e-6, max_value=radius_outer-1e-6, value=(radius_outer+radius_inner)/2,
        help="Punto entre cilindros para evaluar V"
    )
    V = potential_coaxial(charge, length, radius_inner, r_eval) if C else None

    # Resultados
    st.markdown("### Resultados físicos")
    if C and radius_outer > radius_inner:
        st.write(f"**Capacitancia:** {C:.3e} F")
        if V:
            st.write(f"**Potencial en r = {r_eval:.3f} m:** {V:.3e} V")
    else:
        st.error("Verifica todos los parámetros y que b > a.")

    # Gráfico (crear función plot_cylinder en plot_utils.py)
    st.markdown("### Visualización geométrica")
    fig = plot_cylinder(length, radius_inner, radius_outer)
    st.plotly_chart(fig, use_container_width=True)
