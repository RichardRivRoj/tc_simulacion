from fasthtml.common import *
from views.home import home
from views.calc_mm1 import calc_mm1
from views.result_mm1 import result_mm1
from views.calc_mmk import calc_mmk
from views.result_mmk import result_mmk
from views.graph import create_graph
from views.calc_mms import calc_mms
from views.result_mms import result_mms
from views.calc_mmsk import calc_mmsk
from views.result_mmsk import result_mmsk

app, rt = fast_app()

# Rutas 
@rt("/")
def index():
    return home()

@rt("/calc_mm1", methods=["GET"])
def mm1():
    return calc_mm1()

@rt("/result_mm1", methods=["POST", "GET"])
def r_mm1(v_lambda : float, v_mu : float):
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
    
    return result_mm1(v_lambda, v_mu)

@rt("/calc_mmk", methods=["GET"])
def mmk():
    return calc_mmk()

@rt("/result_mmk", methods=["POST", "GET"])
def r_mm1(v_lambda : float, v_mu : float, v_k: int):
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
        
    return result_mmk(v_lambda, v_mu, v_k)

@rt("/calc_mms", methods=["GET"])
def mms():
    return calc_mms()

@rt("/result_mms", methods=["POST", "GET"])
def r_mms(v_lambda : float, v_mu : float, v_c : int):
    
    try:
        v_lambda 
        v_mu
        v_c 
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
    if v_lambda >= v_c * v_mu:
        errores.append("λ debe ser menor que c * μ.")
    if v_c <= 0:
        errores.append("c debe ser mayor a 0")
    if v_c == type(float(v_c)):
        errores.append("c tiene que ser un número entero")

    if errores:
        # Si hay errores, los mostramos en el div de respuesta
        return Div(
            Div(
                *[Div(error, cls="text-red-500") for error in errores], 
                cls="flex flex-col items-center"
            ),
        )   
    return result_mms(v_lambda, v_mu, v_c)


@rt("/calc_mmsk", methods=["GET"])
def mmsk():
    return calc_mmsk()

@rt("/result_mmsk", methods=["POST", "GET"])
def r_mmsk(v_lambda : float, v_mu : float, v_c : int, v_k : int):
    
    try:
        v_lambda 
        v_mu
        v_c 
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
    if v_lambda >= v_c * v_mu:
        errores.append("λ debe ser menor que c * μ.")
    if v_c <= 0:
        errores.append("c debe ser mayor a 0")
    if v_c == type(float(v_c)):
        errores.append("c tiene que ser un número entero")
    if v_k <= v_c:
        errores.append("K debe ser mayor que c")
    if v_k == type(float(v_k)) or v_k <= 0:
        errores.append("K tiene que ser un número entero mayor a 0")

    if errores:
        # Si hay errores, los mostramos en el div de respuesta
        return Div(
            Div(
                *[Div(error, cls="text-red-500") for error in errores], 
                cls="flex flex-col items-center"
            ),
        ) 
        
    return result_mmsk(v_lambda, v_mu, v_c, v_k)

@rt("/graph", methods=['GET', "POST"])
def graph(x_data: str, y_data: str, title: str, x_label: str, y_label: str):
    return create_graph(x_data, y_data, title, x_label, y_label)

serve()