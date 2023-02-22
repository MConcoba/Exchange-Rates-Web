import json
import re

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
        print("Fecha: " + date + " Moneda " +
              i + " " + str(df_rates["Tasas"][i]))


def run():
    fechas = []

    start = True

    print('-----Bienvenido-----')
    while start:
        print('Seleccionar una opccion')
        print('1)  Ingresar una fecha')
        print('2)  Cosultar datos')
        print('3)  Limpiar fechas')

        opt = input('   =>  ')
        rep = True
        if opt == '1':
            while rep:
                print('La fecha debe de complir el siguente formato YYYY-mm-dd')
                date = input('   =>  ')
                if date in fechas:
                    print('La fecha ingreasa ya existe')
                    rep = True
                else:
                    if validateDate(date):
                        fechas.append(date)
                        rep = False
                        print('Desea agregar otra fecha')
                        more = input('yes / no  =>  ')

                        if more == 'yes':
                            rep = True
                        else:
                            start = True
                    else:
                        rep = True
        elif opt == '2':
            if len(fechas) <= 0:
                print('No hay fechas ingresadas')
                start = True
            else:
                for i in range(len(fechas)):
                    obtenerCambios(fechas[i])
        elif opt == '3':
            fechas.clear()


def validateDate(date):
    if re.match(r'^\d{4}-\d{2}-\d{2}$', date):
        return True
    else:
        return False


run()
