import os

import requests
import json
from dotenv import load_dotenv
# API Ninjas key:
load_dotenv()
API_KEY = os.getenv('API_KEY')

BASE_URL = "https://api.api-ninjas.com/v1/"


def fetches_data_via_GET(animal : str):
    request_URL = f"{BASE_URL}animals?name={animal}"
    headers = {"X-Api-Key": API_KEY}
    print("Making the following request", request_URL)
    animals = requests.get(request_URL, headers)
    print("Result of the request: ", end="")
    if "200" in animals.text:
        print("GET request successful!")
    animals = animals.json()
    return animals

def fetches_data_from_file(file_path : str, animal : str):
    if animal.lower() != "fox":
        return ""
    with open(file_path, "r") as handle:
        return json.load(handle)

def fetch_data(animal:str):
    #return fetches_data_from_file("animals_data.json", animal)
    return fetches_data_via_GET(animal)
