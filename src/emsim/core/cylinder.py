    from src.emsim.utils.constants import EPSILON_0
    import numpy as np

    def solve_coaxial_cylinder(length=None, r_in=None, r_out=None, capacitance=None, charge=None, voltage=None, area=None, volume=None):
        # C = 2 * pi * e0 * L / ln(b/a)
        # Q = C V
        result = {}

        if capacitance is None and length and r_in and r_out:
            capacitance = 2 * np.pi * EPSILON_0 * length / np.log(r_out / r_in)
        if length is None and capacitance and r_in and r_out:
            length = (capacitance * np.log(r_out / r_in)) / (2 * np.pi * EPSILON_0)

        # Manejos para charge, voltage
        if charge is None and capacitance and voltage is not None:
            charge = capacitance * voltage
        if voltage is None and charge is not None and capacitance:
            voltage = charge / capacitance

        # Área lateral interna (superficie: 2πrL)
        if area is None and r_in and length:
            area = 2 * np.pi * r_in * length
        if r_in is None and area and length:
            r_in = area / (2 * np.pi * length)

        # Volumen del cilindro interno
        if volume is None and r_in and length:
            volume = np.pi * r_in**2 * length
        if r_in is None and volume and length:
            r_in = (volume / (np.pi * length))**0.5

        if capacitance is None and length and r_in and r_out:
            capacitance = 2 * np.pi * EPSILON_0 * length / np.log(r_out / r_in)

        result.update({
            'length': length,
            'r_in': r_in,
            'r_out': r_out,
            'capacitance': capacitance,
            'charge': charge,
            'voltage': voltage,
            'area': area,
            'volume': volume
        })
        return result
