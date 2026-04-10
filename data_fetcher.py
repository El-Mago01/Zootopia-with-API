import requests
# API Ninjas key:
API_KEY = "NGvVjduynuMZhmbQ07E7yQhMLvLZFRXtOB3E3uEp"

BASE_URL = "https://api.api-ninjas.com/v1/"


def fetches_data(animal):
    request_URL = f"{BASE_URL}animals?name={animal}"
    headers = {"X-Api-Key": API_KEY}
    print("Making the following request", request_URL)
    animals = requests.get(request_URL, headers)
    print("Result of the request: ", end="")
    if "200" in animals.text:
        print("GET request successful!")
    animals = animals.json()
    return animals

def fetch_data_from_file(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)

def fetch_data(animal):
    return fetches_data(animal)

