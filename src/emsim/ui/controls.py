import streamlit as st

def float_input(label, default="", help=None, sidebar=True, key=None):
    """
    Entrada numérica flexible:
    - Permite negativos
    - Permite notación científica (ej: 1e-6)
    - Si está vacío, retorna None
    """
    container = st.sidebar if sidebar else st

    value = container.text_input(label, value=str(default), help=help, key=key)

    if value.strip() == "":
        return None

    try:
        return float(value)
    except ValueError:
        container.warning(f"⚠️ '{value}' no es un número válido. Usa formato decimal o científico.")
        return None


# ==============================================
#  📐 CONTROLES PARA PLACAS PARALELAS
# ==============================================
def plates_controls():
    st.sidebar.subheader("Parámetros físicos")

    area = float_input(
        "Área de cada placa [m²]",
        default="0.01",
        help="Área superficial efectiva (ej: 0.01 = 10cm x 10cm)."
    )

    distance = float_input(
        "Distancia entre placas [m]",
        default="0.01",
        help="Separación uniforme entre placas."
    )

    epsilon_r = float_input(
        "Permitividad relativa (εᵣ)",
        default="8.85e-12",
        help="Aire=1.00, papel≈3, vidrio≈5-10, etc."
    )

    voltaje = float_input(
        "Voltaje aplicado [V]",
        default="5.0",
        help="Diferencia de potencial entre placas."
    )

    carga = float_input(
        "Carga en placas [C]",
        default="",
        help="Si se deja vacío, se calcula automáticamente (Q = C·V)."
    )

    return area, distance, epsilon_r, voltaje, carga


# ==============================================
#  ⚫ CONTROLES PARA ESFERA CONDUCTORA
# ==============================================
def sphere_controls():
    st.sidebar.subheader("Parámetros físicos")

    radius = float_input(
        "Radio de la esfera [m]",
        default="0.1",
        help="Radio exterior de la esfera conductora."
    )

    capacitance = float_input(
        "Capacitancia [F]",
        default="",
        help="Déjalo vacío si deseas calcular C."
    )

    charge = float_input(
        "Carga [C]",
        default="",
        help="Déjalo vacío si deseas calcular Q."
    )

    voltage = float_input(
        "Voltaje [V]",
        default="",
        help="Déjalo vacío si deseas calcular V."
    )

    return radius, capacitance, charge, voltage


# ==============================================
#  📡 CONTROLES PARA CILINDRO / COAXIAL
# ==============================================
def cylinder_controls():
    st.sidebar.subheader("Geometría")

    length = float_input(
        "Longitud [m]",
        default="1.0",
        help="Longitud del cilindro."
    )

    r_in = float_input(
        "Radio interior [m]",
        default="0.1",
        help="Radio del conductor interno."
    )

    r_out = float_input(
        "Radio exterior [m]",
        default="0.2",
        help="Radio del conductor externo."
    )

    st.sidebar.subheader("Parámetros eléctricos")

    capacitance = float_input(
        "Capacitancia [F]",
        default="",
        help="Déjalo vacío para calcular C."
    )

    charge = float_input(
        "Carga [C]",
        default="",
        help="Déjalo vacío para calcular Q."
    )

    voltage = float_input(
        "Voltaje [V]",
        default="",
        help="Déjalo vacío para calcular V."
    )

    return length, r_in, r_out, capacitance, charge, voltage
