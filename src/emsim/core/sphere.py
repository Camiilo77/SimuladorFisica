from emsim.utils.constants import EPSILON_0
import numpy as np

def solve_sphere(radius=None, capacitance=None, charge=None, voltage=None, area=None):
    # C = 4 * pi * e0 * r
    # Q = C V
    # V = Q / C
    # area = 4 * pi * r^2
    result = {}

    # Definición básica
    if capacitance is None and radius:
        capacitance = 4 * np.pi * EPSILON_0 * radius
    if radius is None and capacitance:
        radius = capacitance / (4 * np.pi * EPSILON_0)

    if charge is None and capacitance and voltage is not None:
        charge = capacitance * voltage
    if voltage is None and charge is not None and capacitance:
        voltage = charge / capacitance

    # Área superficial
    if area is None and radius:
        area = 4 * np.pi * radius**2
    if radius is None and area:
        radius = (area / (4 * np.pi))**0.5

    if capacitance is None and radius:
        capacitance = 4 * np.pi * EPSILON_0 * radius

    result.update({
        'radius': radius,
        'capacitance': capacitance,
        'charge': charge,
        'voltage': voltage,
        'area': area
    })
    return result
