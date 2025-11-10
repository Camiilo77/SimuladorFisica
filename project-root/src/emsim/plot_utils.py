import plotly.graph_objects as go
import numpy as np

def plot_parallel_plates(area_m2, distance_m, voltage_V=None, field_NC=None):
    import plotly.graph_objects as go
    import numpy as np

    plate_size = np.sqrt(area_m2) if area_m2 > 0 else 0.1
    fig = go.Figure()
    # Placas
    x = [-plate_size/2, plate_size/2]
    y = [-plate_size/2, plate_size/2]
    z1 = np.full((2,2), 0)
    z2 = np.full((2,2), distance_m)
    fig.add_trace(go.Surface(
        x=np.array(x), y=np.array(y), z=z1,
        colorscale="Blues", showscale=False, opacity=0.8
    ))
    fig.add_trace(go.Surface(
        x=np.array(x), y=np.array(y), z=z2,
        colorscale="Reds", showscale=False, opacity=0.8
    ))

    # Flechas distribuidas en malla 2D
    Nx, Ny = 5, 2  # 5 posiciones en x, 2 en y = 10 flechas distribuidas
    xi = np.linspace(x[0]*0.8, x[1]*0.8, Nx)
    yi = np.linspace(y[0]*0.8, y[1]*0.8, Ny)
    z_start = 0.12 * distance_m
    z_end = distance_m - 0.12 * distance_m
    arrow_color = "green"
    arrow_width = 5
    punta_color = "white"
    punta_size = 5  # Más pequeño para la "punta"

    for ix in xi:
        for iy in yi:
            # Línea de la flecha
            fig.add_trace(go.Scatter3d(
                x=[ix, ix],
                y=[iy, iy],
                z=[z_start, z_end],
                mode='lines',
                line=dict(color=arrow_color, width=arrow_width),
                hoverinfo='none',
                showlegend=False
            ))
            # Punta de flecha pequeña y clara
            fig.add_trace(go.Scatter3d(
                x=[ix],
                y=[iy],
                z=[z_end],
                mode='markers',
                marker=dict(size=punta_size, color=punta_color, symbol="diamond"),
                hoverinfo='text',
                text=["Campo E: de placa - a +"],
                showlegend=False
            ))

    fig.update_layout(
        scene=dict(
            xaxis_title="x (m)", yaxis_title="y (m)", zaxis_title="z (m)",
            aspectratio=dict(x=1, y=1, z=0.16),
            camera=dict(eye=dict(x=1.4, y=1.6, z=0.8))
        ),
        title="Campo eléctrico entre placas paralelas"
    )
    return fig
def plot_sphere(radius_m, charge=None, field_NC=None):
    import plotly.graph_objects as go
    import numpy as np

    # Blindaje para radio
    if radius_m is None or radius_m <= 0:
        radius_m = 0.05  # Valor estándar visible

    phi, theta = np.mgrid[0:np.pi:8j, 0:2*np.pi:12j]
    x = radius_m * np.sin(phi) * np.cos(theta)
    y = radius_m * np.sin(phi) * np.sin(theta)
    z = radius_m * np.cos(phi)

    fig = go.Figure()
    fig.add_trace(go.Surface(
        x=x, y=y, z=z, showscale=False, colorscale="YlGnBu", opacity=0.82
    ))

    punta_size = 5
    for i in range(phi.shape[0]):
        for j in range(theta.shape[1]):
            x0, y0, z0 = x[i, j], y[i, j], z[i, j]
            x1, y1, z1 = x0 * 1.22, y0 * 1.22, z0 * 1.22
            fig.add_trace(go.Scatter3d(
                x=[x0, x1],
                y=[y0, y1],
                z=[z0, z1],
                mode="lines",
                line=dict(color="green", width=5),
                hoverinfo='none',
                showlegend=False
            ))
            fig.add_trace(go.Scatter3d(
                x=[x1], y=[y1], z=[z1],
                mode="markers",
                marker=dict(size=punta_size, color="orange", symbol="diamond"),
                hoverinfo="text",
                text=["Campo E radial"],
                showlegend=False
            ))

    fig.update_layout(
        scene=dict(
            xaxis_title="x (m)", yaxis_title="y (m)", zaxis_title="z (m)",
            aspectmode='cube',
            camera=dict(eye=dict(x=2, y=1.6, z=1.2))
        ),
        title="Esfera conductora y campo radial"
    )
    return fig


#cilindro
def plot_cylinder(length_m, r_in_m, r_out_m):
    import plotly.graph_objects as go
    import numpy as np

    # Blindaje para valores inválidos
    if length_m is None or length_m <= 0:
        length_m = 0.1       # valor estándar mínimo
    if r_in_m is None or r_in_m <= 0:
        r_in_m = 0.01        # radio interno mínimo
    if r_out_m is None or r_out_m <= 0 or r_out_m <= r_in_m:
        r_out_m = r_in_m + 0.01   # radio externo mayor, mínimo

    z = np.linspace(0, length_m, 24)
    theta = np.linspace(0, 2*np.pi, 12)
    theta_grid, z_grid = np.meshgrid(theta, z)
    x1 = r_in_m * np.cos(theta_grid)
    y1 = r_in_m * np.sin(theta_grid)
    z1 = z_grid
    x2 = r_out_m * np.cos(theta_grid)
    y2 = r_out_m * np.sin(theta_grid)
    z2 = z_grid

    fig = go.Figure()
    fig.add_trace(go.Surface(
        x=x1, y=y1, z=z1, showscale=False, colorscale="Blues", opacity=0.8
    ))
    fig.add_trace(go.Surface(
        x=x2, y=y2, z=z2, showscale=False, colorscale="Oranges", opacity=0.45
    ))

    # Flechas radiales distribuidas
    n_arrows = 10
    z_arrows = np.linspace(length_m*0.15, length_m*0.85, 4)
    punta_size = 5
    for mid_z in z_arrows:
        for angle in np.linspace(0, 2*np.pi, n_arrows, endpoint=False):
            x0 = r_in_m * np.cos(angle)
            y0 = r_in_m * np.sin(angle)
            x1_v = r_out_m * np.cos(angle)
            y1_v = r_out_m * np.sin(angle)
            fig.add_trace(go.Scatter3d(
                x=[x0, x1_v], y=[y0, y1_v], z=[mid_z, mid_z],
                mode='lines',
                line=dict(color="green", width=5),
                hoverinfo='none',
                showlegend=False
            ))
            fig.add_trace(go.Scatter3d(
                x=[x1_v], y=[y1_v], z=[mid_z],
                mode="markers",
                marker=dict(size=punta_size, color="white", symbol="diamond"),
                hoverinfo="text",
                text=["Campo E radial"],
                showlegend=False
            ))

    fig.update_layout(
        scene=dict(
            xaxis_title="x (m)", yaxis_title="y (m)", zaxis_title="z (m)",
            aspectmode="cube",
            camera=dict(eye=dict(x=2.2, y=2.1, z=0.7))
        ),
        title="Cilindros coaxiales y campo radial"
    )
    return fig
