import plotly.graph_objects as go
import numpy as np

def plot_parallel_plates(area_m2, distance_m, voltage_V=None, field_NC=None):
    """
    Genera gráfico Plotly 3D de dos placas paralelas y, opcionalmente, el campo eléctrico.
    """
    # Placas como rectángulos, centradas en el eje z con separación 'distance_m'
    plate_size = np.sqrt(area_m2) if area_m2 > 0 else 0.1
    x = [-plate_size/2, plate_size/2]
    y = [-plate_size/2, plate_size/2]
    z1 = np.full((2,2), 0)
    z2 = np.full((2,2), distance_m)
    
    fig = go.Figure()

    # Placa inferior
    fig.add_trace(go.Surface(
        x=np.array(x), y=np.array(y), z=z1,
        colorscale="Blues", showscale=False, name="Placa -",
        opacity=0.7
    ))

    # Placa superior
    fig.add_trace(go.Surface(
        x=np.array(x), y=np.array(y), z=z2,
        colorscale="Reds", showscale=False, name="Placa +",
        opacity=0.7
    ))

    # Campo eléctrico como vectores
    if field_NC is not None and voltage_V is not None:
        # Dibuja flechas ideales en mitad de espacio entre placas
        n_arrows = 8
        xi = np.linspace(x[0], x[1], n_arrows)
        yi = np.linspace(y[0], y[1], n_arrows)
        zi = np.full(n_arrows, distance_m/2)
        fig.add_trace(go.Cone(
            x=xi, y=yi, z=zi,
            u=np.zeros(n_arrows), v=np.zeros(n_arrows), w=np.full(n_arrows, field_NC),
            colorscale="Viridis", showscale=False, sizemode="absolute", sizeref=0.2,
            name="Campo E"
        ))

    fig.update_layout(
        scene=dict(
            xaxis_title="x (m)", yaxis_title="y (m)", zaxis_title="z (m)",
            aspectratio=dict(x=1, y=1, z=0.25)
        ),
        title="Placas paralelas - Geometría y campo ideal"
    )
    return fig
import plotly.graph_objects as go
import numpy as np

def plot_sphere(radius_m, charge=None):
    """
    Grafica una esfera conductora 3D y (opcionalmente) algunos vectores del campo externo.
    """
    # Malla para la esfera
    phi, theta = np.mgrid[0:np.pi:20j, 0:2*np.pi:40j]
    x = radius_m * np.sin(phi) * np.cos(theta)
    y = radius_m * np.sin(phi) * np.sin(theta)
    z = radius_m * np.cos(phi)

    fig = go.Figure()

    # Superficie de la esfera
    fig.add_trace(go.Surface(
        x=x, y=y, z=z, showscale=False, colorscale="YlGnBu", opacity=0.8, name="Superficie"
    ))

    # Campo eléctrico: flechas partiendo de la superficie (si hay carga)
    if charge is not None:
        n_arrows = 15
        angles = np.linspace(0, 2*np.pi, n_arrows)
        for angle in angles:
            # Vector radial desde superficie hacia fuera
            x0, y0, z0 = radius_m*np.cos(angle), radius_m*np.sin(angle), 0
            x1, y1, z1 = 1.2*radius_m*np.cos(angle), 1.2*radius_m*np.sin(angle), 0.0
            fig.add_trace(go.Scatter3d(
                x=[x0, x1], y=[y0, y1], z=[z0, z1],
                mode='lines+markers',
                line=dict(color="red", width=6),
                marker=dict(size=2),
                showlegend=False
            ))

    fig.update_layout(
        scene=dict(
            xaxis_title="x (m)", yaxis_title="y (m)", zaxis_title="z (m)",
            aspectmode='cube'
        ),
        title="Esfera conductora"
    )
    return fig
def plot_cylinder(length_m, r_in_m, r_out_m):
    """
    Grafica dos cilindros coaxiales (interno y externo) en 3D.
    """
    z = np.linspace(0, length_m, 50)
    theta = np.linspace(0, 2 * np.pi, 50)
    theta_grid, z_grid = np.meshgrid(theta, z)

    # Cilindro interno
    x1 = r_in_m * np.cos(theta_grid)
    y1 = r_in_m * np.sin(theta_grid)
    z1 = z_grid

    # Cilindro externo
    x2 = r_out_m * np.cos(theta_grid)
    y2 = r_out_m * np.sin(theta_grid)
    z2 = z_grid

    fig = go.Figure()

    # Añadir cilindro interior
    fig.add_trace(go.Surface(
        x=x1, y=y1, z=z1, showscale=False, colorscale="Blues", opacity=0.75,
        name="Cilindro interno"
    ))

    # Añadir cilindro exterior
    fig.add_trace(go.Surface(
        x=x2, y=y2, z=z2, showscale=False, colorscale="Oranges", opacity=0.45,
        name="Cilindro externo"
    ))

    fig.update_layout(
        scene=dict(
            xaxis_title="x (m)", yaxis_title="y (m)", zaxis_title="z (m)",
            aspectmode="cube"
        ),
        title="Cilindros coaxiales"
    )
    return fig
