from fasthtml import FastHTML
from fasthtml.common import *
from component.header import header
from component.footer import footer
<<<<<<< HEAD
from component.main import main_layout
=======
from layout.main_layout import main_layout
>>>>>>> 98dbc5503002defbcda4c59e8dca8f9c14210e7b

app, rt = fast_app()

@rt("/")
def index():
<<<<<<< HEAD
    # Crear el formulario directamente con clases de Python
=======
    # Vista Principal: Muestra las opciones que se pueden calcular
>>>>>>> 98dbc5503002defbcda4c59e8dca8f9c14210e7b
    return Html(
        Head(
            Link(rel="stylesheet", href="/static/output.css"),
            Title("Inicio")
        ),
        Body(
            Div(
<<<<<<< HEAD
              header(),
                Div(
                    main_layout(),
                    cls="container mx-auto p-6 flex-grow"
                ), 
            footer(),
            cls="flex flex-col min-h-screen"  
=======
                header(),
                    Div(
                        main_layout(),
                        cls="container mx-auto p-6 flex-grow"
                    ), 
                footer(),
                cls="flex flex-col min-h-screen"  
>>>>>>> 98dbc5503002defbcda4c59e8dca8f9c14210e7b
            ),
            cls="m-0"
        ),      
    )

@rt("/calcularmm1", methods=["GET"])
def calcular_cola():
<<<<<<< HEAD
    
    form = Form(
        Label("Tasa de llegada: ", Input(name="tasa_llegada", type="number", cls="border p-2")),
        Div("Tasa de servicio: ", Input(name="tasa_servicio", type="number", cls="border p-2")),
        Div("Servidores: ", Input(name="servidores", type="number", cls="border p-2")),
        Button("Calcular", type="submit", cls="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"),
        action = '/result_MM1',
        method="POST",
        cls= "pl-5 space-y-4"
=======
    # Vista Calculadora M/M/1: Permite introducir las variables para calcular M/M/1
    form = Div(
        Form(
            H2("M/M/1", cls="font-medium text-black text-center"),
            Label("Tasa de llegada: ", Input(name="tasa_llegada", type="number", cls="flex rounded-md border mt-2 px-3 py-1"), cls="block font-medium text-black"),
            Label("Tasa de servicio: ", Input(name="tasa_servicio", type="number", cls="flex rounded-md border mt-2 px-3 py-1"), cls="block font-medium text-black"),
            Label("Servidores: ", Input(name="servidores", type="number", cls="flex rounded-md border mt-2 px-3 py-1"), cls="block font-medium text-black"),
            Button("Calcular", type="submit", cls="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center"),
            action = '/result_MM1',
            method="POST",
            cls= "space-y-6"
        ),
        cls="p-6 bg-white border border-gray-200 rounded-lg shadow"
>>>>>>> 98dbc5503002defbcda4c59e8dca8f9c14210e7b
    )
    
    return Html(
        Head(
            Link(rel="stylesheet", href="/static/output.css"),
            Title("Calculadora de Teoria de Colas")
        ),
        Body(
            Div(
<<<<<<< HEAD
              header(),
                Div(
                    form,
                    cls="container mx-auto p-6 flex-grow"
                ), 
=======
                header(),
                    Div(
                        form,
                        cls="container flex justify-center mx-auto p-6 flex-grow"
                    ), 
>>>>>>> 98dbc5503002defbcda4c59e8dca8f9c14210e7b
            footer(),
            cls="flex flex-col min-h-screen"  
            ),
            cls="m-0"
        ),      
    )

@rt("/result_MM1", methods=["POST"])
def resultado(tasa_llegada : float, tasa_servicio : float, servidores : int):
    
    # Cálculos de teoría de colas
    rho = tasa_llegada / (servidores * tasa_servicio)
    vacio = (1 - rho)
    
    resultado = Div(
        Div(f"Factor de utilización (rho): {rho:.2f}", cls="text-lg text-green-500"), 
        H2(f"Factor que el servidor este vacio P0: {vacio:.2f}", cls="text-lg text-green-500"),
        Div(
            A('Volver', href='/', cls="text-red-300")
        )
    )
    
    return Html(
        Head(
            Link(rel="stylesheet", href="/static/output.css"),
            Title("Calculadora de Teoria de Colas")
        ),
        Body(
            Div(
<<<<<<< HEAD
              header(),
                Div(
                    resultado,
                    cls="container mx-auto p-6 flex-grow"
                ), 
=======
                header(),
                    Div(
                        resultado,
                        cls="container mx-auto p-6 flex-grow"
                    ), 
>>>>>>> 98dbc5503002defbcda4c59e8dca8f9c14210e7b
            footer(),
            cls="flex flex-col min-h-screen"  
            ),
            cls="m-0"
        ),      
    )
    

serve()