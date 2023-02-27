import json

import pandas as pd
import requests
from datetime import date

dia1 = date(2023, 1, 1) # año - mes - dia
print(dia1)
dias = [date(2023, 1, 1), date(2023, 1, 2)]

for dia in dias:
    url = "https://api.apilayer.com/exchangerates_data/" + dia.strftime('%Y-%m-%d') + "?symbols=JPY,GTQ,BEF,CHF,FRF,CAD,ITL,GBP,DEM,ESP,ATS,NLG,SEK,CRC,SVC,MXP,HNL,NIC,VEB,DKK,EUR,NOK,SDR,IDB,ARP,BRC,KRW,HKD,TWD,CNY,PKR,INR,VEF,COP&base=USD"
    payload = {}
    headers = {"apikey": "x6J5I3oRy4BjphrilXZO5Iha7qGUDJFD"}

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.text
    if response.status_code == 200:
        data = response.json()
        rates = data.get("rates")
        if rates:
            print(f"Fecha: {day}")
            for currency, rate in rates.items():
                print(f"Moneda {currency}: {rate}")
    else:
        print(f"Error al obtener los datos del día {day}")
