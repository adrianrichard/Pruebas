# from kivymd.app import MDApp
# from kivymd.uix.screen import MDScreen
# from kivymd.uix.button import MDRaisedButton
# from kivymd.uix.textfield import MDTextField
# from kivymd.uix.label import MDLabel
# from kivymd.uix.scrollview import MDScrollView
# from kivymd.uix.list import MDList, OneLineListItem
# import requests

# class MundialApp(MDApp):
#     def build(self):
#         # Configuración del tema (colores de la FIFA/Mundial)
#         self.theme_cls.primary_palette = "DeepPurple" 
#         self.theme_cls.theme_style = "Dark"

#         # Pantalla principal
#         screen = MDScreen()

#         # Título
#         screen.add_widget(
#             MDLabel(
#                 text="MUNDIAL 2026",
#                 halign="center",
#                 pos_hint={"center_y": 0.9},
#                 font_style="H4"
#             )
#         )

#         # Botón para consultar
#         btn = MDRaisedButton(
#             text="ACTUALIZAR GRUPOS",
#             pos_hint={"center_x": 0.5, "center_y": 0.8},
#             on_release=self.obtener_datos
#         )
#         screen.add_widget(btn)

#         # Contenedor con scroll para los resultados
#         scroll = MDScrollView(pos_hint={"center_x": 0.5, "center_y": 0.35}, size_hint=(0.9, 0.7))
#         self.lista_resultados = MDList()
#         scroll.add_widget(self.lista_resultados)
#         screen.add_widget(scroll)

#         return screen

#     def obtener_datos(self, *args):
#         self.lista_resultados.clear_widgets()
        
#         url = "https://v3.football.api-sports.io/standings"
#         headers = {
#             'x-rapidapi-host': "v3.football.api-sports.io",
#             'x-rapidapi-key': "b551655b86392050700304822daa5858"
#         }
#         # Nota: Recuerda usar 2022 si sigues en el plan gratuito
#         params = {"league": "1", "season": "2022"}

#         try:
#             res = requests.get(url, headers=headers, params=params)
#             data = res.json()

#             if data.get('response'):
#                 grupos = data['response'][0]['league']['standings']
#                 for grupo in grupos:
#                     # Añadir nombre del grupo como encabezado
#                     self.lista_resultados.add_widget(
#                         OneLineListItem(text=f"--- {grupo[0]['group']} ---")
#                     )
#                     for equipo in grupo:
#                         nombre = equipo['team']['name']
#                         pts = equipo['points']
#                         self.lista_resultados.add_widget(
#                             OneLineListItem(text=f"{equipo['rank']}. {nombre} ({pts} Pts)")
#                         )
#             else:
#                 self.lista_resultados.add_widget(OneLineListItem(text="Error de Plan o Conexión"))
#         except Exception as e:
#             self.lista_resultados.add_widget(OneLineListItem(text="Error de red"))

# if __name__ == "__main__":
#     MundialApp().run()

import flet as ft
import requests

def main(page: ft.Page):
    # Configuración de la página (Vista Móvil)
    page.title = "Mundial 2022"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.spacing = 20
    # Centrar contenido en la pantalla
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Título principal
    titulo = ft.Text(
        "COPA MUNDIAL 2022", 
        size=15, 
        weight=ft.FontWeight.BOLD, 
        color=ft.Colors.AMBER_400
    )

    # Contenedor donde se cargarán los grupos
    lista_grupos = ft.Column(scroll=ft.ScrollMode.ADAPTIVE, expand=True)

    def obtener_datos(e):
        # Limpiamos la lista y mostramos un indicador de carga
        lista_grupos.controls.clear()
        progreso = ft.ProgressBar(width=400, color="amber")
        lista_grupos.controls.append(progreso)
        page.update()

        url = "https://v3.football.api-sports.io/standings"
        headers = {
            'x-rapidapi-host': "v3.football.api-sports.io",
            'x-rapidapi-key': "b551655b86392050700304822daa5858" 
        }
        # Nota: Usamos 2022 por la restricción de tu plan actual
        params = {"league": "1", "season": "2022"}

        try:
            response = requests.get(url, headers=headers, params=params)
            data = response.json()
            lista_grupos.controls.remove(progreso)

            if data.get('response'):
                standings = data['response'][0]['league']['standings']
                print(standings[0])  # Para depuración, puedes eliminarlo después
                
                for grupo in standings:
                    filas_equipos = []
                    # Encabezado de la tabla del grupo
                    filas_equipos.append(
                        ft.DataRow(
                            cells=[                                
                                ft.DataCell(ft.Text("", weight="bold")),
                                ft.DataCell(ft.Text("Equipo", weight="bold")),
                                ft.DataCell(ft.Text("Pts", weight="bold")),
                                ft.DataCell(ft.Text("Dif", weight="bold")),
                                
                            ]
                        )
                    )

                    for equipo in grupo:
                        filas_equipos.append(
                            ft.DataRow(
                                cells=[                                    
                                    ft.DataCell(ft.Image(src=equipo['team']['logo'], width=30, height=30, fit="contain")),
                                    ft.DataCell(ft.Text(equipo['team']['name'])),
                                    ft.DataCell(ft.Text(str(equipo['points']))),
                                    ft.DataCell(ft.Text(equipo['goalsDiff'])),                                                                      
                                    ]
                            )
                        )

                    # Creamos una tarjeta (Card) por cada grupo
                    tarjeta_grupo = ft.Card(
                        content=ft.Container(
                            padding=15,
                            content=ft.Column([
                                ft.Text(grupo[0]['group'], size=20, weight="bold", color="blueaccent"),
                                ft.DataTable(
                                    columns=[
                                        ft.DataColumn(ft.Text("")),
                                        ft.DataColumn(ft.Text("")),
                                        ft.DataColumn(ft.Text("")),
                                        ft.DataColumn(ft.Text("")),
                                    ],
                                    rows=filas_equipos,
                                    heading_row_height=0, # Ocultamos el header default
                                )
                            ])
                        )
                    )
                    lista_grupos.controls.append(tarjeta_grupo)
            else:
                lista_grupos.controls.append(ft.Text("Error: Verifica tu plan de API (2022-2024)"))

        except Exception as ex:
            lista_grupos.controls.append(ft.Text(f"Error de conexión: {ex}"))
        
        page.update()

    # Botón flotante para refrescar
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.REFRESH, 
        bgcolor=ft.Colors.AMBER_400,
        on_click=obtener_datos
    )

    # Agregar elementos a la página
    page.add(
        titulo,
        ft.Text("Posiciones en tiempo real", size=10, color=ft.Colors.GREY_400),
        lista_grupos
    )

# Para correrlo como App de escritorio o web
# ft.app(target=main) 

# Para verlo directamente como si fuera un celular en el navegador:
ft.app(target=main)