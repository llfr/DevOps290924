import requests
from time import sleep

try: 
    response = requests.get("https://goog")
except BaseException as e:
    print(f"Something went wrong {e.args}")

time_to_sleep = input("time_to_sleep: ")
sleep(time_to_sleep)

a = int(input("First: "))
b = int(input("Second: "))
res = a / b
print(res)