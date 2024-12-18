import flet as ft
import sqlite3
def main (page: ft.Page):
    gatos_all=[]
    def conexion():
       return  sqlite3.connect('flet.db')
    def agregar_bd(e):
        conexionbd=conexion()
        conexionbd.execute("INSERT INTO gatos (nombre, color, nacionalidad) VALUES (?,?,?)", (nombre.value, color.value, nacionalidad.value))
        conexionbd.commit()
        conexionbd.close()
    def ir_otra_pag(e):
        all_gatos()
        page.views.append( ft.View(route="/all_gatos", controls=[
            
            ft.TextButton(text="regresar", on_click=regresar_pagina), 
            *gatos_all
        ]) )
        page.update()
        
    def all_gatos():
        conexion_bd=(conexion()).execute("select * from gatos")
        lista=conexion_bd.fetchall()
        conexion_bd.close()
        gatos_all.clear()
        for i, fila in enumerate(lista):
            gatos_all.append( ft.Text(value=f"Fila {i}: {fila}"))
            
    def regresar_pagina(e):
        page.views.pop()
        page.update()
    nombre=ft.TextField(value="", max_length=20)
    color=ft.TextField(value="", max_length=20)
    nacionalidad=ft.TextField(value="", max_length=20)
    page.add(ft.Column(controls=[
        ft.Text(value="Ingresa el nombre"),
        nombre,
        ft.Text(value="Ingresa el color de tu gatito"), 
        color,
        ft.Text(value="Ingresa su nacionalidad"),
        nacionalidad,
        ft.TextButton(text="Agregar a la bd", on_click=agregar_bd)

    ]  ))
    page.add(ft.Row(controls=[
        ft.TextButton(text="ver todos los gatos", tooltip="ir a la otra pagina ", on_click=ir_otra_pag)
    ],alignment=ft.MainAxisAlignment.CENTER  )  )
ft.app(main)
