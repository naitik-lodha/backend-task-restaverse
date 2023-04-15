import requests
import pandas as pd
import json


def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        # If the Nested key-value pair is of dict type
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        # If the Nested key-value pair is of list type
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


restaurant_id =input()
header = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0"}
response = requests.get(
    f"https://www.swiggy.com/dapi/menu/pl?page-type=REGULAR_MENU&complete-menu=true&lat=18.56&lng=73.95&restaurantId={restaurant_id}",
    headers=header)

# Parse the response body as JSON
json_data = json.loads(response.text)

# Extract the required JSON object from the parsed response
menu_data = json_data["data"]["cards"]


# Flatten the extracted JSON object
flattened_data = flatten_json(menu_data)

# Normalize the flattened JSON object
df = pd.json_normalize(menu_data)
df.to_csv("data.csv")
