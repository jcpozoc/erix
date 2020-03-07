import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Quito"
dest = "Ibarra"
key = "AGyS3P5dtnyEMNxGmio8x1FfLqpURZGu"

url = main_api + urllib.parse.urlencode({"key" : key, "from":orig, "to":dest})

json_data = requests.get(url).json()

print(json_data)