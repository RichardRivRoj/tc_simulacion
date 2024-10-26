from fasthtml.common import *
from layouts.guest_layout import guest_layout
from components.buttons import calculation_button

def home():
    # Vista Principal: Muestra las opciones que se pueden calcular
    return guest_layout(
        Div(
            H2(
                "CALCULADORA DE TEORÍA DE COLAS", 
                cls="bg-blue-800 text-white font-bold p-4 rounded text-center text-base"
            ),
            Div(
                # Fila de cálculos simples
                Div(
                    H3("SIMPLE", cls="bg-blue-600 text-white text-center py-4 rounded-t-md font-bold"),
                    Div(
                        calculation_button("ℹ️", "M/M/1", "Población infinita canal simple", "bg-white", "text-black", "bl", "/calc_mm1"),
                        calculation_button("ℹ️", "M/M/1/DG/K/∞", "Población finita canal simple", "bg-white", "text-black", "br", "/calc_mmk"),
                        cls="grid grid-cols-2 rounded-md shadow-sm"
                    ),
                    cls="rounded-md overflow-hidden"
                ),
                # Fila de cálculos múltiples
                Div(
                    H3("MULTIPLE", cls="bg-blue-600 text-white text-center py-4 rounded-t-md font-bold"),
                    Div(
                        calculation_button("⚠️", "EN DESAROLLO", "Próximamente", "bg-white", "text-black", "bl", "#"),
                        calculation_button("⚠️", "EN DESAROLLO", "Próximamente", "bg-white", "text-black", "br", "#"),
                        cls="grid grid-cols-2 rounded-md shadow-sm"
                    ),
                    cls="rounded-md overflow-hidden"
                ),
                cls="space-y-8 mt-8"
            ),
            cls="container mx-auto py-6 px-16"
        ),
        title="Inicio"
    )
