import requests

def getPoke(poke):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    

    http://www.omdbapi.com/?apikey=[yourkey]&
    http://img.omdbapi.com/?apikey=[yourkey]&