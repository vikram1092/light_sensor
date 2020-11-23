import requests

# Change the following values to make sense for you after completing set up
ip_address = 'YOU_IP_ADDRESS'
username = 'YOUR_USERNAME'
number = '1'

putRequest = 'http://{}/api/{}/lights/{}/state'.format(
    ip_address,
    username,
    number
)

getRequest = 'http://{}/api/{}/lights'.format(
    ip_address,
    username
)

def get_light_state():
    r = requests.get(getRequest)
    print(r.json)
    light = r.json()[number]
    state = light["state"]
    return state["on"]


def toggle_light(value):
    lightIsOn = get_light_state()

    if lightIsOn != value:
        headers = {"Content-Type":"application/json"}
        params = {"on":value}

        r = requests.put(
            putRequest, 
            headers = headers, 
            json = params
        )