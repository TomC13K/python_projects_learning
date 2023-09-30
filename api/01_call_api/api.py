import requests

def get_data():
    url = 'https://ipinfo.io/json'
    
    response = ""
    try:
        response = requests.get(url)
    except:
        print("Unknown error in communicating with the API")
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Error while calling API")
        return None


ip_info = get_data()
    
    
    
    