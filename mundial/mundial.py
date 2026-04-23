import requests

def obtener_grupos_online():
    # Configuración de la API (API-Football es un estándar de la industria)
    url = "https://v3.football.api-sports.io/standings"
    
    # IMPORTANTE: Necesitas tu propia API KEY de api-football.com
    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': "845c400af86b5b1fed06c0f5d97a0cbc" 
    }
    
    # Parámetros para el Mundial 2026 (League ID 1 suele ser el Mundial)
    querystring = {"league": "1", "season": "2026"}

    try:
        print("Conectando con la base de datos del Mundial...")
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()

        if response.status_code == 200 and data['response']:
            standings = data['response'][0]['league']['standings']
            
            print(f"\n{' RESULTADOS OFICIALES 2026 ':*^40}\n")
            for grupo in standings:
                nombre_grupo = grupo[0]['group']
                print(f"--- {nombre_grupo} ---")
                for equipo in grupo:
                    rank = equipo['rank']
                    nombre = equipo['team']['name']
                    puntos = equipo['points']
                    print(f"{rank}. {nombre} | Pts: {puntos}")
                print("-" * 25)
        else:
            print("Error: No se pudieron obtener los datos. Revisa tu API Key.")

    except Exception as e:
        print(f"Error de conexión: {e}")

if __name__ == "__main__":
    obtener_grupos_online()