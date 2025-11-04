import numpy as np

# Constantes físicas
EPSILON_0 = 8.854e-12  # Vacío [F/m]

def capacitance_parallel_plates(area_m2, distance_m, epsilon_r=1.0):
    """
    Calcula la capacitancia para placas paralelas.
    area_m2: área de las placas (m²)
    distance_m: distancia entre placas (m)
    epsilon_r: permitividad relativa del material intermedio
    return: capacitancia (Farads)
    """
    if area_m2 <= 0 or distance_m <= 0 or epsilon_r <= 0:
        return None
    return EPSILON_0 * epsilon_r * area_m2 / distance_m

def electric_field_parallel_plates(voltage_V, distance_m):
    """
    Calcula el campo eléctrico entre placas ideales.
    voltage_V: diferencia de potencial (V)
    distance_m: separación entre placas (m)
    return: campo eléctrico (N/C)
    """
    if distance_m == 0:
        return None
    return voltage_V / distance_m

def potential_parallel_plates(charge_C, capacitance_F):
    """
    Calcula el potencial entre placas dado Q y C.
    charge_C: carga entre placas (Coulomb)
    capacitance_F: capacitancia (Farads)
    """
    if capacitance_F == 0:
        return None
    return charge_C / capacitance_F

def latex_deduction():
    """
    Devuelve la deducción de la fórmula en formato LaTeX para la UI.
    """
    return r"""
    \[
    C = \varepsilon_0\,\varepsilon_r\,\frac{A}{d}
    \]
    Donde:
    - \(C\) = capacitancia [F]
    - \(\varepsilon_0\) = permitividad del vacío (\(8.854 \times 10^{-12} \,\text{F/m}\))
    - \(\varepsilon_r\) = permitividad relativa del dieléctrico
    - \(A\) = área de cada placa [m²]
    - \(d\) = distancia entre placas [m]
    """
