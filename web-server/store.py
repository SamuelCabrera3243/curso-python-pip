import requests

#obtener categorias de una pagina web con request, haciendo un GET

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text) #formato str
    categories = r.json()
    for category in categories:
        print(category['name'])