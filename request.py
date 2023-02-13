import json

import requests

from env import key_api


def getData(start, end):
    url = "https://api.apilayer.com/exchangerates_data/timeseries?start_date=" + \
          start+"&end_date="+end+"&base=USD&symbols=JPY,GTQ,BEF,CHF,FRF,CAD,ITL,GBP,DEM,ESP,ATS,NLG,SEK,CRC,SVC,MXP,HNL,NIC,VEB,DKK,EUR,NOK,SDR,IDB,ARP,BRC,KRW,HKD,TWD,CNY,PKR,INR,VEF,COP"

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
                    'valor': valor,
                } for iso, valor in monedas.items()
            ]
        } for fecha, monedas in rates.items()
    ]

    return resultado
