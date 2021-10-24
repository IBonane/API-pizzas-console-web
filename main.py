import requests
import json

url = "https://pizzalistmenu.herokuapp.com/api/getpizzas"

data = requests.get(url)

pizzas = json.loads(data.text)

print('\n----------liste des pizzas-----------')

for pizzaModel in pizzas:
    pizza = pizzaModel['fields']
    print(pizza['nom']+' ---------> '+str(pizza['prix'])+' €')

