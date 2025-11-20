# Simulador Interactivo de Capacitancia y Potencial

Simulador educativo en Streamlit para calcular y visualizar la capacitancia, potencial y campo eléctrico en **placas paralelas**, **esferas conductoras** y **cilindros coaxiales**. Incluye deducciones en LaTeX y gráficas interactivas 3D con Plotly.

---

## Estructura del proyecto


---

## Instalación

1. Clona este repositorio.
2. Instala dependencias:
    ```
    pip install -r requirements.txt
    ```
3. Ejecuta la app:
    ```
    streamlit run src/app.py
    ```

---

## Características

- Cálculo de \(C\), \(V\), \(\vec{E}\) en sistemas ideales.
- Visualización 3D interactiva con Plotly.
- Deducción teórica para cada caso en formato LaTeX.
- Tests unitarios listos en `tests/`.

---

## Despliegue en Streamlit Cloud

1. Sube tu código a GitHub.
2. Ve a [streamlit.io/cloud](https://streamlit.io/cloud) y crea app nueva.
   - Archivo principal: `src/app.py`
3. Listo para compartir vía URL pública.

---

## Créditos

- Autor: [Tu Nombre]
- Licencia: MIT

---

## Notas
- Todos los valores en unidades del SI.
- Requiere Python 3.8+.

