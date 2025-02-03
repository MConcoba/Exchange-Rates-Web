import requests
import json
import pandas as pd
import random


from Lista_circular import listacircular
mylista = listacircular()

#url = "https://api.apilayer.com/exchangerates_data/timeseries?start_date=2023-02-01&end_date=2023-02-10"
#?symbols=JPY,GTQ,BEF,CHF,FRF,CAD,ITL,GBP,DEM,ESP,ATS,NLG,SEK,CRC,SVC,MXP,HNL,NIC,VEB,DKK,EUR,NOK,SDR,IDB,ARP,BRC,KRW,HKD,TWD,CNY,PKR,INR,VEF,COP&base=USD

def obtenercambios(dates):
    for date in dates:
        url = "https://api.apilayer.com/exchangerates_data/" + date + \
            "?symbols=JPY,GTQ,BEF,CHF,FRF,CAD,ITL,GBP,DEM,ESP,ATS,NLG,SEK,CRC,SVC,MXP,HNL,NIC,VEB,DKK,EUR,NOK,SDR,IDB,ARP,BRC,KRW,HKD,TWD,CNY,PKR,INR,VEF,COP&base=USD"

        payload = {}
        headers = {"apikey": "5RgLWSXp7Cdo5zr64ZcC1yJfXuKhLpZY"}

        response = requests.request("GET", url, headers=headers, data=payload)

        status_code = response.status_code
        result = response.text
        # Convertir cadena de caracteres JSON a un diccionario
        datos_diccionario = json.loads(result)
        fecha = datos_diccionario["date"]
        rates = datos_diccionario["rates"]
        for moneda, valor in rates.items():
          mylista.agregarinicio(fecha, moneda, round(valor, 2))

    return mylista.Recorrer()
    
