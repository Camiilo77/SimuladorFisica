def positive_value(value, name):
    """
    Valida que el parámetro sea positivo.
    """
    if value is None or value <= 0:
        return f"El parámetro '{name}' debe ser mayor que cero."
    return None

def check_cylinder(r_in, r_out):
    """
    Valida radios de cilindro coaxial.
    """
    err = []
    if r_in <= 0:
        err.append("El radio interior debe ser mayor a cero.")
    if r_out <= r_in:
        err.append("El radio exterior debe ser mayor al interior.")
    return err if err else None
