from fasthtml.common import *

def tabla_resultado(headers: list, data: list):
    """
    Genera una tabla reutilizable con FastHTML y TailwindCSS, con un estilo formal, estructurado
    y con soporte para scroll si los datos son extensos.
    
    Parámetros:
    - headers: Lista con los nombres de las columnas.
    - data: Lista de diccionarios donde cada diccionario representa una fila con los datos.
    """
    return Div(
        Div(  # Contenedor para el scroll
            Table(
                Thead(
                    Tr(
                        *[Th(header, cls="px-6 py-3 border-b border-gray-300 bg-gray-100 text-left text-sm font-semibold text-gray-700 uppercase tracking-wider") for header in headers]
                    )
                ),
                Tbody(
                    *[
                        Tr(
                            *[Td(f"{fila[columna]}", cls="px-6 py-4 border-b border-gray-200 text-sm text-gray-900 text-right") for columna in fila],
                            cls="bg-white hover:bg-gray-50" if i % 2 == 0 else "bg-gray-50 hover:bg-gray-100"
                        ) for i, fila in enumerate(data)
                    ]
                ),
                cls="min-w-full border-collapse bg-white border border-gray-300 shadow-md rounded-lg overflow-hidden",
            ),
            cls="overflow-auto max-h-64"  # Permitir scroll y limitar la altura máxima
        ),
        cls="rounded-lg border border-gray-300 shadow-md"  # Estilo del contenedor principal
    )