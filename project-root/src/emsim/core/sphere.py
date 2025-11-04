import numpy as np

# Constantes físicas
EPSILON_0 = 8.854e-12  # Vacío [F/m]

def capacitance_sphere(radius_m):
    """
    Calcula la capacitancia de una esfera conductora aislada.
    radius_m: radio de la esfera (m)
    return: capacitancia (Farads)
    """
    if radius_m <= 0:
        return None
    return 4 * np.pi * EPSILON_0 * radius_m

def potential_sphere(charge_C, radius_m):
    """
    Calcula el potencial eléctrico en la superficie de una esfera cargada.
    charge_C: carga total en la esfera (C)
    radius_m: radio (m)
    return: potencial sobre la superficie (V)
    """
    if radius_m == 0:
        return None
    return (1 / (4 * np.pi * EPSILON_0)) * (charge_C / radius_m)

def electric_field_outside_sphere(charge_C, radius_eval_m):
    """
    Campo eléctrico fuera de la esfera: se comporta como carga puntual.
    charge_C: carga total (C)
    radius_eval_m: distancia desde el centro (m)
    return: campo eléctrico (N/C)
    """
    if radius_eval_m == 0:
        return None
    return (1 / (4 * np.pi * EPSILON_0)) * (charge_C / radius_eval_m**2)

def latex_deduction():
    """
    Devuelve deducción LaTeX para capacitancia de esfera.
    """
    return r"""
    \[
    C = 4\pi\varepsilon_0\,r
    \]
    Donde:
    - \(C\) = capacitancia [F]
    - \(\varepsilon_0\) = permitividad del vacío (\(8.854 \times 10^{-12} \,\text{F/m}\))
    - \(r\) = radio de la esfera [m]
    """
