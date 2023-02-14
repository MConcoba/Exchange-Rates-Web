import json

import pandas as pd
import requests
import tableprint

from env import key_api, url_api


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
                    'valor': round(valor, 2),
                } for iso, valor in monedas.items()
            ]
        } for fecha, monedas in rates.items()
    ]

    pd.set_option('display.max_rows', 1500)
    df = pd.DataFrame(
        [(d['fecha'], x['iso'], round(x['valor'], 2))
            for d in resultado for x in d['monedas']],
        columns=['Fecha', 'Moneda', 'Valor']
    )

    data = [(d['fecha'], x['iso'], round(x['valor'], 2))
            for d in resultado for x in d['monedas']]
    headers = ['Fecha', 'Moneda', 'Valor']

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
   #S print(resultado)
    
    return resultado
