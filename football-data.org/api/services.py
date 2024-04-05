import requests

def get_username():
    url = "https://api.football-data.org/v4/matches"
    headers = { 'X-Auth-Token' : '7ea9c80b36364478940b361b2dcaa23f'
}
    data = requests.get(url, headers=headers)
    if data.status_code == 200:
        return data.json()['matches']
    
    else:
        return print("No hay acceso a la API")
        
        
    