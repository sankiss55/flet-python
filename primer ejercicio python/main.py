import flet as ft

def main(page: ft.Page):
    page.bgcolor="#7a4be7"
    page.title = "primer ejercicio flet de python 😀"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    def plus_text(e):
        if(int(texto.value)==0):
            texto_secundario.visible=False
        texto.value=str(int(texto.value)+1)
        page.update()
    def remover_plus(e):
        if(int(texto.value)==0):
            texto_secundario.visible=True
        else:
            texto.value=str(int(texto.value)-1)
            
            
        page.update()
    def hola(e):
        boton2.icon_size=24
        page.update()
    boton2= ft.IconButton(ft.icons.REMOVE, on_click=remover_plus, icon_color="#eff159")
    boton4=ft.IconButton(ft.icons.ADD, on_click=plus_text,icon_color="#eff159",on_focus=hola)
    texto=ft.Text(value="0")
    texto_secundario=ft.Text(value="no se puede numero menores de 0",visible=False, color="red")
    page.add(
        ft.Row(controls=[
            boton4,
            texto,
            boton2
        ],
            alignment=ft.MainAxisAlignment.CENTER
            ),
        ft.Row(controls=[
            texto_secundario
        ],alignment=ft.MainAxisAlignment.CENTER)
    )
   
ft.app(main)