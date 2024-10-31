from fasthtml.common import *
from components.header import header
from components.footer import footer

def guest_layout(content, title):
    return Html(
        Head(
            Link(rel="stylesheet", href="/static/output.css"),
            Link(rel="icon", type="image/ico", href="/static/img/icono_linesim.ico"),
            Script(src="https://unpkg.com/htmx.org@1.5.0"),
            Script(src="https://cdn.plot.ly/plotly-latest.min.js"),
            Title(title)
        ),
        Body(
            Div(
                header(),
                content,
                footer(),
                cls="flex flex-col min-h-screen"  
            ),
            cls="m-0"
        ),      
    )