#creamos un entorno vistual 
# python -m venv venv              python -m venv venv
#activate cd venv/Scripts activate 

import flet as ft

def main(page: ft.Page):
    page.add(ft.Text("Hola, Flet"))

ft.app(main)
