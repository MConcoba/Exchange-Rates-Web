import json
import os
import pandas as pd
import requests
# import tableprint

from env import key_api, url_api
from controllers.cirucular_double_controller import CircularDouble

lista = CircularDouble()


def getData(start, end, coins):
    lista.clear()
    url = url_api + "/timeseries?start_date=" + start+"&end_date="+end + \
        "&base=USD&symbols="+coins
    payload = {}
    headers = {
        "apikey": key_api
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    status_code = response.status_code
    if status_code == 200:
        result = response.text
        datos = json.loads(result)
        rates = datos['rates']

        i = 1
        exchange_reates = []
        id_counter = 1
        for date, values in rates.items():
            for iso, value in values.items():
                
                exchange_reates.append({
                    'id': id_counter,
                    'date': date,
                    'iso': iso,
                    'country': '',
                    'value': round(value, 2)
                })
                id_counter += 1
        symbols = getSymbols()  # Obtener la lista de símbolos

        for i in exchange_reates:
            for s in symbols:
                if s['value'] == i['iso']:
                    # Buscar el país y asignar su valor
                    i['country'] = s['label']

        for x in range(len(exchange_reates)):
            lista.add(exchange_reates[x], 'last')

        os.system('cls')
        now = datetime.now()

        print('*'*100)
        print('INFORMACION DEL PRIMER DATO')
        print('     Valor', lista.first.data)
        print('     Siguiente', lista.first.next.data)
        print('     Anterior', lista.first.prev.data) 
        print('_'*100)
        print('INFORMACION DEL ULTIMO DATO')
        print('     Valor', lista.last.data)
        print('     Siguiente', lista.last.next.data)
        print('     Anterior', lista.last.prev.data)

        print('*'*100)
       # lista.get_random_list()
        return lista.show_group_from_init()
    else:
        return {'status': False, 'message': 'Error al obtener los datos'}


def get_ramdom():
    return lista.get_random_list()


def getSymbols():
    url = url_api + "/symbols"

    payload = {}
    headers = {
        "apikey": key_api
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    result = response.text
    datos = json.loads(result)
    symbols = datos['symbols']
    resultado = [
        {
            'value': iso,
            'label': nombre
        } for iso, nombre in symbols.items()
    ]
    # print(resultado)
    return resultado


def find_currencies_labels(data, monedas):
    def find_label(currency):
        for item in data:
            if item['value'] == currency:
                return item['label']
        return None

    results = []
    currencies = monedas.split(',')
    for currency in currencies:
        label = find_label(currency)
        if label:
            results.append({'currency': currency, 'label': label})
        else:
            results.append({'currency': currency, 'label': None})
    return results
