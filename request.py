import json

import pandas as pd
import requests
import tableprint

from env import key_api, url_api
from cirucular_double_controller import CircularDouble

lista = CircularDouble()


def getData(start, end, coins):
    url = url_api + "/timeseries?start_date=" + start+"&end_date="+end + \
        "&base=USD&symbols="+coins
    payload = {}
    headers = {
        "apikey": key_api
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    result = response.text
    datos = json.loads(result)
    rates = datos['rates']
    resultado = [
        {
            'fecha': fecha,
            'monedas': [
                {
                    'iso': iso,
                    'pais': '',
                    'valor': round(valor, 2),
                } for iso, valor in monedas.items()
            ]
        } for fecha, monedas in rates.items()
    ]

    symbols = getSymbols()  # Obtener la lista de símbolos

    for r in resultado:
        for m in r['monedas']:
            for s in symbols:
                if s['value'] == m['iso']:
                    m['pais'] = s['label']  # Buscar el país y asignar su valor

    data = [(d['fecha'], x['iso'], x['pais'], round(x['valor'], 2))
            for d in resultado for x in d['monedas']]
    headers = ['Fecha', 'Moneda ISO', 'Nombre Moneda', 'Valor']

    newDa = [
        {
            'date': f['fecha'],
            'iso': x['iso'],
            'country': x['pais'],
            'value': round(x['valor'], 2),
        } for f in resultado for x in f['monedas']
    ]

    for x in range(len(newDa)):
        lista.add_last(newDa[x])

    print('------------ Cambios de USD ------------')
    # print(newDa[0])
    # print(data[0]['fecha']['monedas'][0])
    # tableprint.table(data, headers)
    lista.show_from_init()
    print("________________________________________")
    return resultado


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
