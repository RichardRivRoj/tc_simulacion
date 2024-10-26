from fasthtml.common import *

def calculation_button(icon, title, subtitle, bg_color, text_color, border_radius_dir, dir):
    return A(
        Div(
            icon, 
            cls="text-3xl w-16"
        ),
        Div(
            Div(title, cls="text-lg font-bold"),
            Div(subtitle, cls="text-sm text-gray-600"),
            cls="flex flex-col justify-center"
        ),
        cls=f"flex flex-row items-center px-4 py-2 text-sm font-medium {text_color} {bg_color} border border-gray-200 rounded-{border_radius_dir}-lg hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700",
        href=f'{dir}'
    )