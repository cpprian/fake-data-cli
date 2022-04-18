import requests, random

if __name__ == "__main__":
    size = 3
    url_name = f"https://random-data-api.com/api/name/random_name?size={size}"
    url_address = f"https://random-data-api.com/api/address/random_address?size={size}"
    response_name = requests.get(url_name)
    response_address = requests.get(url_address)
    
    
    for i in range(size):
        age = random.randint(18, 100)
        print(f"Name: {response_name.json()[i]['name']} \tAddress: {response_address.json()[i]['city']} \tAge: {age}")