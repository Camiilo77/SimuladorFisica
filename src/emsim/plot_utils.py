import plotly.graph_objects as go
import numpy as np

def plot_parallel_plates(area_m2, distance_m, voltage_V=None, field_NC=None):
    """Placas paralelas 3D con Plotly"""
    plate_size = np.sqrt(area_m2) if area_m2 > 0 else 0.1
    fig = go.Figure()
    
    # Placas como superficies
    x = np.array([-plate_size/2, plate_size/2])
    y = np.array([-plate_size/2, plate_size/2])
    z1 = np.array([[0, 0], [0, 0]])
    z2 = np.array([[distance_m, distance_m], [distance_m, distance_m]])
    
    fig.add_trace(go.Surface(
        x=x, y=y, z=z1,
        colorscale="Blues", showscale=False, opacity=0.9, name='Placa -'
    ))
    fig.add_trace(go.Surface(
        x=x, y=y, z=z2,
        colorscale="Reds", showscale=False, opacity=0.9, name='Placa +'
    ))
    
    # Flechas distribuidas
    Nx, Ny = 5, 3
    xi = np.linspace(x[0]*0.8, x[1]*0.8, Nx)
    yi = np.linspace(y[0]*0.8, y[1]*0.8, Ny)
    z_start = 0.15 * distance_m
    z_end = distance_m - 0.15 * distance_m
    
    for ix in xi:
        for iy in yi:
            # Línea de flecha
            fig.add_trace(go.Scatter3d(
                x=[ix, ix],
                y=[iy, iy],
                z=[z_start, z_end],
                mode='lines+markers',
                line=dict(color='lime', width=7),
                marker=dict(size=[0, 10], color='lime', symbol='diamond'),
                hoverinfo='text',
                text='Campo E',
                showlegend=False
            ))
    
    fig.update_layout(
        title=f'Placas Paralelas | Área: {area_m2:.4f} m² | Distancia: {distance_m:.6f} m',
        scene=dict(
            xaxis_title='X (m)',
            yaxis_title='Y (m)',
            zaxis_title='Z (m)',
            aspectmode='auto',
            camera=dict(eye=dict(x=1.5, y=1.5, z=1.2)),
            bgcolor='rgba(30, 30, 30, 0.9)'
        ),
        height=700,
        paper_bgcolor='#1a1a1a',
        font=dict(color='#fff'),
        showlegend=True
    )
    return fig

def plot_sphere(radius_m, charge=None, field_NC=None):
    """Esfera conductora 3D con Plotly"""
    if radius_m is None or radius_m <= 0:
        radius_m = 0.05
    
    # Malla esfera más densa
    phi, theta = np.mgrid[0:np.pi:30j, 0:2*np.pi:40j]
    x = radius_m * np.sin(phi) * np.cos(theta)
    y = radius_m * np.sin(phi) * np.sin(theta)
    z = radius_m * np.cos(phi)
    
    fig = go.Figure()
    
    # Superficie esfera
    fig.add_trace(go.Surface(
        x=x, y=y, z=z,
        colorscale='Viridis',
        showscale=True,
        opacity=0.95,
        name='Esfera',
        colorbar=dict(thickness=15, len=0.7)
    ))
    
    # Vectores radiales del campo
    punta_size = 9
    step = 3  # Cada 3 puntos para no saturar
    for i in range(0, phi.shape[0], step):
        for j in range(0, phi.shape[1], step):
            x0, y0, z0 = x[i, j], y[i, j], z[i, j]
            x1, y1, z1 = x0 * 1.4, y0 * 1.4, z0 * 1.4
            
            fig.add_trace(go.Scatter3d(
                x=[x0, x1],
                y=[y0, y1],
                z=[z0, z1],
                mode='lines+markers',
                line=dict(color='lime', width=6),
                marker=dict(size=[0, punta_size], color='lime', symbol='diamond'),
                hoverinfo='text',
                text='Campo E',
                showlegend=False
            ))
    
    fig.update_layout(
        title=f'Esfera Conductora | Radio: {radius_m:.4f} m',
        scene=dict(
            xaxis_title='X (m)',
            yaxis_title='Y (m)',
            zaxis_title='Z (m)',
            aspectmode='cube',
            camera=dict(eye=dict(x=1.5, y=1.5, z=1.2)),
            bgcolor='rgba(30, 30, 30, 0.9)'
        ),
        height=700,
        paper_bgcolor='#1a1a1a',
        font=dict(color='#fff'),
        showlegend=True
    )
    return fig

def plot_cylinder(length_m, r_in_m, r_out_m):
    """Cilindros coaxiales 3D con Plotly"""
    if length_m is None or length_m <= 0:
        length_m = 0.1
    if r_in_m is None or r_in_m <= 0:
        r_in_m = 0.01
    if r_out_m is None or r_out_m <= 0 or r_out_m <= r_in_m:
        r_out_m = r_in_m + 0.01
    
    # Mallas cilindros
    z = np.linspace(0, length_m, 30)
    theta = np.linspace(0, 2*np.pi, 40)
    theta_grid, z_grid = np.meshgrid(theta, z)
    
    x1 = r_in_m * np.cos(theta_grid)
    y1 = r_in_m * np.sin(theta_grid)
    z1 = z_grid
    
    x2 = r_out_m * np.cos(theta_grid)
    y2 = r_out_m * np.sin(theta_grid)
    z2 = z_grid
    
    fig = go.Figure()
    
    # Superficies cilindros
    fig.add_trace(go.Surface(
        x=x1, y=y1, z=z1,
        colorscale='Blues',
        showscale=False,
        opacity=0.95,
        name='Cilindro interior'
    ))
    fig.add_trace(go.Surface(
        x=x2, y=y2, z=z2,
        colorscale='Oranges',
        showscale=False,
        opacity=0.8,
        name='Cilindro exterior'
    ))
    
    # Vectores radiales
    n_arrows = 12
    z_arrows = np.linspace(length_m*0.15, length_m*0.85, 5)
    punta_size = 9
    
    for mid_z in z_arrows:
        for angle in np.linspace(0, 2*np.pi, n_arrows, endpoint=False):
            x0 = r_in_m * np.cos(angle)
            y0 = r_in_m * np.sin(angle)
            x1_v = r_out_m * np.cos(angle)
            y1_v = r_out_m * np.sin(angle)
            
            fig.add_trace(go.Scatter3d(
                x=[x0, x1_v],
                y=[y0, y1_v],
                z=[mid_z, mid_z],
                mode='lines+markers',
                line=dict(color='lime', width=6),
                marker=dict(size=[0, punta_size], color='lime', symbol='diamond'),
                hoverinfo='text',
                text='Campo E',
                showlegend=False
            ))
    
    fig.update_layout(
        title=f'Cilindro Coaxial | L: {length_m:.4f} m | r_in: {r_in_m:.4f} m | r_out: {r_out_m:.4f} m',
        scene=dict(
            xaxis_title='X (m)',
            yaxis_title='Y (m)',
            zaxis_title='Z (m)',
            aspectmode='auto',
            camera=dict(eye=dict(x=1.5, y=1.5, z=1.2)),
            bgcolor='rgba(30, 30, 30, 0.9)'
        ),
        height=700,
        paper_bgcolor='#1a1a1a',
        font=dict(color='#fff'),
        showlegend=True
    )
    return fig
