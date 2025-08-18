import requests

base_url =""

def get_json_info(name):
    url = f"{base_url}"
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        print("Retrieved the data")
    else:
        print(f"Failed to retrieve the data{response.status_code}")


json_name = "iotgw"
get_json_info(json_name)










