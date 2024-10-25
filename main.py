from fasthtml import FastHTML
from fasthtml.common import *
import json
from views.home import home
from views.calcular_cola import calcular_cola
from views.result_mm1 import resultado_mm1
from views.calcular_colak import calcular_colak
from views.result_mm1k import resultado_mm1k
from views.graficas import crear_grafica

import plotly.graph_objects as go

app, rt = fast_app()

# Rutas 

@rt("/")
def index():
    return home()

@rt("/calcularmm1", methods=["GET"])
def mm1():
    return calcular_cola()

@rt("/result_MM1", methods=["POST", "GET"])
def result_mm1(v_lambda : float, v_mu : float):
    try:
        v_lambda 
        v_mu 
    except ValueError:
        return Div(
            Div(
                P("Error: Los valores ingresados deben ser numéricos.", cls="text-red-500 text-center"),
                cls="bg-white p-4 rounded-lg shadow-md border max-w-md mx-auto mt-4"
            )
        )

    # Validar los valores
    errores = []
    if v_lambda <= 0:
        errores.append("λ debe ser mayor a 0.")
    if v_mu <= 0:
        errores.append("μ debe ser mayor a 0.")
    if v_lambda >= v_mu:
        errores.append("λ debe ser menor que μ.")

    if errores:
        # Si hay errores, los mostramos en el div de respuesta
        return Div(
            Div(
                *[Div(error, cls="text-red-500") for error in errores], 
                cls="flex flex-col items-center"
            ),
            cls="overflow-hidden mb-auto bg-white border border-gray-200 rounded-lg shadow"
        )
    
    return resultado_mm1(v_lambda, v_mu)

@rt("/calcularmm1k", methods=["GET"])
def mm1k():
    return calcular_colak()

@rt("/result_MM1K", methods=["POST", "GET"])
def result_mm1(v_lambda : float, v_mu : float, v_k : int):
    
    try:
        v_lambda 
        v_mu 
    except ValueError:
        return Div(
            Div(
                P("Error: Los valores ingresados deben ser numéricos.", cls="text-red-500 text-center"),
                cls="bg-white p-4 rounded-lg shadow-md border max-w-md mx-auto mt-4"
            )
        )

    # Validar los valores
    errores = []
    if v_lambda <= 0:
        errores.append("λ debe ser mayor a 0.")
    if v_mu <= 0:
        errores.append("μ debe ser mayor a 0.")
    if v_lambda >= v_mu:
        errores.append("λ debe ser menor que μ.")
    if v_k <= 0:
        errores.append("K debe ser mayor a 0")
    if v_k == type(float(v_k)):
        errores.append("K tiene que ser un número entero")

    if errores:
        # Si hay errores, los mostramos en el div de respuesta
        return Div(
            Div(
                *[Div(error, cls="text-red-500") for error in errores], 
                cls="flex flex-col items-center"
            ),
            cls="overflow-hidden mb-auto bg-white border border-gray-200 rounded-lg shadow"
        )
        
    return resultado_mm1k(v_lambda, v_mu, v_k)

@rt("/grafica", methods=['GET', "POST"])
def vista_grafica(x_data: str, y_data: str, title: str, x_label: str, y_label: str):
    return crear_grafica(x_data, y_data, title, x_label, y_label)

serve()