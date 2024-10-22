import plotly.graph_objects as go
from fasthtml import *

def crear_grafica(x_data, y_data, title, x_label, y_label):
    """
    Crea un gráfico utilizando Plotly y devuelve el código HTML para embebido.
    
    Parámetros:
    - x_data: Datos para el eje X.
    - y_data: Datos para el eje Y.
    - title: Título de la gráfica.
    - x_label: Etiqueta para el eje X.
    - y_label: Etiqueta para el eje Y.
    """
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_data, y=y_data, mode='lines+markers', name=y_label))
    fig.update_layout(
        title=title,
        xaxis_title=x_label,
        yaxis_title=y_label,
        height=350,  # Ajustar la altura de las gráficas
        margin=dict(l=20, r=20, t=50, b=50)
    )
    return fig.to_html(full_html=False)