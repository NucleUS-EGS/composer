# generate data

import requests

URL = 'http://localhost:8080'
# URL = 'http://grupo5-egs-deti.ua.pt/'

# Generate events
ENDPOINT = '/events/v1/events'

data = [
	{
		'name': 'Febrada',
		'description': 'Febrada do DETI',
		'date': '2024-05-30',
		'location': 'DETI',
		'price': 10.0,
		'type': 'Convívio',
		'points': 10
	},
	{
		'name': 'Jantar de Gala',
		'description': 'Jantar de Gala do DETI',
		'date': '2024-06-30',
		'location': 'DETI',
		'price': 20.0,
		'type': 'Gala',
		'points': 20
	},
	{
		'name': 'Festa de Natal',
		'description': 'Festa de Natal do DETI',
		'date': '2024-12-30',
		'location': 'DETI',
		'price': 5.0,
		'type': 'Festa',
		'points': 5
	}
]

for event in data:
	response = requests.post(f'{URL}{ENDPOINT}', json=event)
	print(response.json())