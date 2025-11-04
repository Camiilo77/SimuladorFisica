import numpy as np

# Constantes físicas
EPSILON_0 = 8.854e-12  # Vacío [F/m]

def capacitance_coaxial_cylinder(length_m, radius_inner_m, radius_outer_m, epsilon_r=1.0):
    """
    Calcula la capacitancia de un cilindro coaxial por unidad de longitud.
    length_m: largo del cilindro (m)
    radius_inner_m: radio interno (m)
    radius_outer_m: radio externo (m)
    epsilon_r: permitividad relativa
    return: capacitancia (Farads)
    """
    if length_m <= 0 or radius_inner_m <= 0 or radius_outer_m <= 0 or radius_inner_m >= radius_outer_m or epsilon_r <= 0:
        return None
    return (2 * np.pi * EPSILON_0 * epsilon_r * length_m) / np.log(radius_outer_m / radius_inner_m)

def potential_coaxial(charge_C, length_m, radius_inner_m, radius_eval_m):
    """
    Potencial entre cilindros.
    charge_C: carga total (C)
    length_m: largo (m)
    radius_inner_m: radio del cilindro interior (m)
    radius_eval_m: radio donde se evalúa el potencial (m)
    return: potencial eléctrico (V)
    """
    if length_m <= 0 or radius_inner_m <= 0 or radius_eval_m <= radius_inner_m:
        return None
    return (charge_C / (2 * np.pi * EPSILON_0 * length_m)) * np.log(radius_eval_m / radius_inner_m)

def latex_deduction():
    """
    Devuelve deducción LaTeX para la capacitancia de cilindro coaxial.
    """
    return r"""
    \[
    C = \frac{2\pi\varepsilon_0\varepsilon_r\,L}{\ln(b/a)}
    \]
    Donde:  
    - \(C\): capacitancia [F]  
    - \(\varepsilon_0\): permitividad del vacío  
    - \(\varepsilon_r\): permitividad relativa  
    - \(L\): longitud del cilindro [m]  
    - \(a\): radio interior [m]  
    - \(b\): radio exterior [m]
    """
