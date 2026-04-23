import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Clima Global - AdriaTech"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Ajustes de ventana
    page.window.width = 400
    page.window.height = 600
    page.window.resizable = False
    # El centrado no es necesario, la ventana aparece en posición predeterminada

    # Componentes
    input_ciudad = ft.TextField(
        label="Ciudad o País",
        width=300,
        border_radius=15
    )
    
    label_temp = ft.Text(value="", size=40, weight=ft.FontWeight.BOLD)
    label_desc = ft.Text(value="", size=18, italic=True)
    
    def consultar(e):
        if not input_ciudad.value:
            label_temp.value = "Escribe algo..."
            label_desc.value = ""
            page.update()
            return

        api_key = "a7b14871853e0167e104f780fd608acf" 
        url = f"http://api.openweathermap.org/data/2.5/weather?q={input_ciudad.value}&appid={api_key}&units=metric&lang=es"
        
        try:
            r = requests.get(url, timeout=10)
            data = r.json()
            if data["cod"] == 200:
                temp = data["main"]["temp"]
                desc = data["weather"][0]["description"]
                label_temp.value = f"{temp}°C"
                label_desc.value = desc.capitalize()
                label_temp.color = ft.Colors.ORANGE_700
            else:
                label_temp.value = "No encontrado"
                label_desc.value = ""
                label_temp.color = ft.Colors.RED_700
        except:
            label_temp.value = "Error de red"
            label_desc.value = ""
            label_temp.color = ft.Colors.RED_700
        
        page.update()

    # Interfaz
    page.add(
        ft.Icon(ft.Icons.WB_SUNNY, color=ft.Colors.AMBER, size=70),
        ft.Text("Consultar Clima", size=25, weight=ft.FontWeight.BOLD),
        input_ciudad,
        ft.FilledButton("Obtener datos", on_click=consultar),
        ft.Divider(height=40, color=ft.Colors.TRANSPARENT),
        label_temp,
        label_desc
    )

if __name__ == "__main__":
    ft.app(target=main)