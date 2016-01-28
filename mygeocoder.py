import requests
import json
from pprint import pprint

with open("dummy.txt") as f:
	for line in f:
			
		url = 'https://geocoder.cit.api.here.com/6.2/geocode.json'
		payload = {'searchtext': line, 'app_id': '1uUn6h6dokUhd1LIdF1K', 'app_code': 'P-7t4eyPupFp-s8jtHRLjA', 'gen': '0'}
		
		# GET with params in URL
		r = requests.get(url, params=payload)
		
		if (r.status_code==200) :
			data = json.loads(r.text)
			try:
				data = data["Response"]["View"][0]["Result"][0]["Location"]["DisplayPosition"]
			except IndexError :
				print("Error")
				continue
			
			print(str(data["Latitude"])+","+str(data["Longitude"]))
			
		else :
			print("Error")
			continue
		
