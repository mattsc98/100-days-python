import requests

pixela_endpoint = 'https://pixe.la/v1/users'

TOKEN = 'abfhsk345fjaf78fda45'
USERNAME = 'matthew98'

user_params = {
    "token"                 : TOKEN,
    "username"              : USERNAME,
    "agreeTermsOfService"   : "yes",
    "notMinor"              : "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

GRAPH_ID = 'graph1'
GRAPH_NAME = "Gooning Graph"
GRAPH_UNIT = "Liters"
GRAPH_UNIT_TYPE = "float"
GRAPH_COLOR = "kuro"

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    "id"    : GRAPH_ID,
    "name"  : GRAPH_NAME,
    "unit"  : GRAPH_UNIT,
    "type"  : GRAPH_UNIT_TYPE,
    "color" : GRAPH_COLOR
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)