import requests
import json
import pandas as pd
from datetime import date

dia1 = date(2023, 2, 1) # año - mes - dia
print(dia1)
dias = [date(2023, 1, 1), date(2023, 1, 2)]


#url = "https://api.apilayer.com/exchangerates_data/timeseries?start_date=2023-05-01&end_date=2023-05-10"
url = "https://api.apilayer.com/exchangerates_data/"+dia1.strftime('%Y-%m-%d')+"?symbols=JPY,GTQ,BEF,CHF,FRF,CAD,ITL,GBP,DEM,ESP,ATS,NLG,SEK,CRC,SVC,MXP,HNL,NIC,VEB,DKK,EUR,NOK,SDR,IDB,ARP,BRC,KRW,HKD,TWD,CNY,PKR,INR,VEF,COP&base=USD"

payload = {}
headers= {
  "apikey": "LNu91jNIyHZ0O2YHXTTxzZ15ZHwOX28i"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
# Convertir cadena de caracteres JSON a un diccionario
datos_diccionario = json.loads(result)


df = pd.DataFrame(datos_diccionario)
#df_rates = df['rates']
df_rates=pd.DataFrame({"Tasas":df['rates']})


for i in df_rates.index: 
     print("Moneda " + i + " " + str(df_rates["Tasas"][i]))