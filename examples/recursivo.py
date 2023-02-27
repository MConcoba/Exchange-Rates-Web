import json
from datetime import date, datetime, timedelta

import pandas as pd
import requests


def obtenerCambios(date: date, number):

    if number == 0:
        return
    else:
        url = "https://api.apilayer.com/exchangerates_data/" + date.strftime('%Y-%m-%d') + \
            "?symbols=JPY,GTQ,BEF,CHF,FRF,CAD,ITL,GBP,DEM,ESP,ATS,NLG,SEK,CRC,SVC,MXP,HNL,NIC,VEB,DKK,EUR,NOK,SDR,IDB,ARP,BRC,KRW,HKD,TWD,CNY,PKR,INR,VEF,COP&base=USD"

        payload = {}
        headers = {"apikey": "x6J5I3oRy4BjphrilXZO5Iha7qGUDJFD"}

        response = requests.request("GET", url, headers=headers, data=payload)

        status_code = response.status_code
        result = response.text
        # Convertir cadena de caracteres JSON a un diccionario

        datos_diccionario = json.loads(result)
        rates = datos_diccionario['rates']
        resultado = [
            {
                'fecha': date.strftime('%Y-%m-%d'),
                'moneda': moneda,
                'valor': round(valor, 2),
            } for moneda, valor in rates.items()
        ]

        pd.set_option('display.max_rows', 1500)
        df = pd.DataFrame(
            [(d['fecha'], d['moneda'], d['valor'])
                for d in resultado],
            columns=['Fecha', 'Moneda', 'Valor']
        )

        print(df)

        date = date + timedelta(days=1)
        obtenerCambios(date, number-1)


dia = date(2023, 1, 1)
obtenerCambios(dia, 5)
