import requests

#Before
my_file = open("names.txt", "r")
names = my_file.read().splitlines()
for name in names:
    print(name)

my_file.close()

#After
with open("names.txt", "r") as my_file:
    names = my_file.read().splitlines()
    for name in names:
        print(name)

with requests.get("https://google1.com/") as response:
    response.raise_for_status() #Raises an error when the response is not 200(OK)