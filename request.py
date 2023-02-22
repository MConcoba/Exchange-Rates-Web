import json

import pandas as pd
import requests
import tableprint

from env import key_api, url_api


def getData(start, end, coins):
    url = f"{url_api}/timeseries?start_date={start}&end_date={end}&base=USD&symbols={coins}"
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

    pd.set_option('display.max_rows', 1500)
    df = pd.DataFrame(
        [(d['fecha'], x['iso'], x['pais'], round(x['valor'], 2))
            for d in resultado for x in d['monedas']],
        columns=['Fecha', 'Moneda ISO', 'Nombre Moneda', 'Valor']
    )

    data = [(d['fecha'], x['iso'], x['pais'], round(x['valor'], 2))
            for d in resultado for x in d['monedas']]
    headers = ['Fecha', 'Moneda ISO', 'Nombre Moneda', 'Valor']

    print('------------ Cambios de USD ------------')
    # print(df)
    tableprint.table(data, headers)
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
