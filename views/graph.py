import plotly.graph_objects as go
import json

def create_graph(x_data: list, y_data: list, title: str, x_label: str, y_label: str):
    # Crear la gráfica
    x_data = list(json.loads(x_data))
    y_data = list(json.loads(y_data))

    if isinstance(x_data, str):
        x_data = x_data.strip('[]').split(',')
        x_data = [float(x.strip()) for x in x_data if x.strip()]

    if isinstance(y_data, str):
        y_data = y_data.strip('[]').split(',')  # Elimina los corchetes y divide por comas
        y_data = [float(y.strip()) for y in y_data if y.strip()]  # Convierte a float cada elemento y elimina espacios

    fig_2 = go.Figure()
    fig_2.add_trace(
        go.Bar(
            x=x_data,
            y=y_data,
            name='M/M/1',
            marker_color='#2563EB'
        )
    )

    fig_2.add_trace(
        go.Scatter(
            x=x_data,
            y=y_data,
            mode='lines+markers',
            name='Linea',
            marker_color='#B91C1C'
        )
    )

    fig_2.update_layout(
        title=title,
        xaxis_title=x_label,
        yaxis_title=y_label,
        autosize=False,
        width=500,  
        height=300,
        barmode='group',
        template='plotly_white',
        xaxis=dict(
            tickmode='array',
            tickvals=x_data
        )
    )

    # Obtener el HTML de la gráfica
    grafica_html = fig_2.to_html(full_html=False, include_plotlyjs='cdn')
    return grafica_html