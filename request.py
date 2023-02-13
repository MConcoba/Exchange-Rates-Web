import json

import pandas as pd
import requests
import tableprint

from env import key_api, url_api


def getData(start, end):
    url = url_api + "/timeseries?start_date=" + start+"&end_date="+end + \
        "&base=USD&symbols=JPY,GTQ,BEF,CHF,FRF,CAD,ITL,GBP,DEM,ESP,ATS,NLG,SEK,CRC,SVC,MXP,HNL,NIC,VEB,DKK,EUR,NOK,SDR,IDB,ARP,BRC,KRW,HKD,TWD,CNY,PKR,INR,VEF,COP"

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
    headers = ['No.' 'Fecha', 'Moneda', 'Valor']

    # print(df)
    tableprint.table(data, headers)

    return resultado
