import streamlit as st
from emsim.core.sphere import capacitance_sphere, potential_sphere, electric_field_outside_sphere, latex_deduction
from emsim.plot_utils import plot_sphere  # Debes crear esta función para la gráfica 3D
import numpy as np

def main():
    st.markdown("## Capacitancia de Esfera Conductora")
    st.markdown("### Deducción y fórmula")
    st.latex(latex_deduction())

    st.sidebar.subheader("Parámetros físicos")
    radius = st.sidebar.number_input(
        "Radio de la esfera [m]", min_value=0.0001, value=0.05,
        help="Radio de la esfera conductora"
    )
    charge = st.sidebar.number_input(
        "Carga total [C]", value=1e-9,
        help="Carga depositada en la esfera"
    )

    # Cálculos
    C = capacitance_sphere(radius)
    V = potential_sphere(charge, radius) if C else None
    r_eval = st.sidebar.number_input(
        "Distancia radial para campo externo [m]", min_value=radius+1e-6, value=radius+0.02,
        help="Punto para evaluar el campo fuera de la esfera (r > radio)"
    )
    E = electric_field_outside_sphere(charge, r_eval) if r_eval and charge else None

    # Resultados
    st.markdown("### Resultados físicos")
    if C:
        st.write(f"**Capacitancia:** {C:.3e} F")
        st.write(f"**Potencial en la superficie:** {V:.3e} V")
        if E:
            st.write(f"**Campo eléctrico fuera (r = {r_eval:.3f} m):** {E:.3e} N/C")
    else:
        st.error("Verifica que el radio sea positivo.")

    # Gráfico (crear o adaptar la función plot_sphere en plot_utils.py)
    st.markdown("### Visualización geométrica y campo")
    fig = plot_sphere(radius, charge)
    st.plotly_chart(fig, use_container_width=True)
