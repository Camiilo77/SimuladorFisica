from src.emsim.utils.constants import EPSILON_0

# Dado cualquier combinación de (area, distance, capacitance, voltage, charge), calcula los otros posibles
def solve_parallel_plates(area=None, distance=None, capacitance=None, voltage=None, charge=None):
    # C = e0 * A / d
    # Q = C * V
    # V = Q / C
    # A = C * d / e0
    # d = e0 * A / C
    
    

    result = {}

    # Determinaciones secuenciales
    if capacitance is None and area and distance:
        capacitance = EPSILON_0 * area / distance
    if area is None and capacitance and distance:
        area = (capacitance * distance) / EPSILON_0
    if distance is None and capacitance and area:
        distance = (EPSILON_0 * area) / capacitance

    # Volver a intentar capacitance si ahora tenemos area o distance
    if capacitance is None and area and distance:
        capacitance = EPSILON_0 * area / distance

    # Cálculos relacionados con Q, V, C
    if charge is None and capacitance and voltage is not None:
        charge = capacitance * voltage
    if voltage is None and charge is not None and capacitance:
        voltage = charge / capacitance
    if capacitance is None and charge is not None and voltage is not None:
        capacitance = charge / voltage

    # Campo eléctrico ideal
    if voltage is not None and distance:
        field = voltage / distance
    else:
        field = None

    # Resumen
    result.update({
        'area': area,
        'distance': distance,
        'capacitance': capacitance,
        'voltage': voltage,
        'charge': charge,
        'field': field
    })
    return result


