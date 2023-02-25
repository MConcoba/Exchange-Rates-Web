import json

import pandas as pd
import requests


def obtenerCambios(date):
    url = "https://api.apilayer.com/exchangerates_data/" + date + \
        "?symbols=JPY,GTQ,BEF,CHF,FRF,CAD,ITL,GBP,DEM,ESP,ATS,NLG,SEK,CRC,SVC,MXP,HNL,NIC,VEB,DKK,EUR,NOK,SDR,IDB,ARP,BRC,KRW,HKD,TWD,CNY,PKR,INR,VEF,COP&base=USD"

    payload = {}
    headers = {"apikey": "x6J5I3oRy4BjphrilXZO5Iha7qGUDJFD"}

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.text
    # Convertir cadena de caracteres JSON a un diccionario
    datos_diccionario = json.loads(result)

    df = pd.DataFrame(datos_diccionario)
    # df_rates = df['rates']
    df_rates = pd.DataFrame({"Tasas": df['rates']})

    for i in df_rates.index:
        print("Fecha de cambio: " + dia.strftime('%Y-%m-%d') + " Moneda " + i + " " + str(df_rates["Tasas"][i]))


days = ['2023-01-02', '2023-01-03', '2023-01-04']

for i in range(len(days)):
    obtenerCambios(days[i])
