from fasthtml import FastHTML
from fasthtml.common import *
from views.home import home
from views.calcular_cola import calcular_cola
from views.result_mm1 import resultado_mm1

app, rt = fast_app()

# Rutas 

@rt("/")
def index():
    return home()

@rt("/calcularmm1", methods=["GET"])
def mm1():
    return calcular_cola()

@rt("/result_MM1", methods=["POST"])
def result_mm1(v_lambda : float, v_mu : float):
    return resultado_mm1(v_lambda, v_mu)

serve()