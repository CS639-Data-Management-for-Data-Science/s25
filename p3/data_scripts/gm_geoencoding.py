import googlemaps
from datetime import datetime
import json
import os
import datetime
from tqdm import tqdm

gmaps = googlemaps.Client(key='Some-KEY')
DATA_SRC = "/home/agarg54/p4_cs639/data/jsons"


if __name__ == "__main__":
    pbar = tqdm(total=len(os.listdir(DATA_SRC)))
    for js in sorted(os.listdir(DATA_SRC)):
        # print(js)
        if js.endswith(".json"):
            pbar.set_description(f"Processing {js}")
            with open(os.path.join(DATA_SRC, js)) as f:
                data = json.load(f)
                for place in data['places']:
                    if "formattedAddress" in place:
                        # print(place["formattedAddress"])
                        geocode_result = gmaps.geocode(place["formattedAddress"])
                        # print(geocode_result)
                        place["geocode_result"] = geocode_result
                        # print(place)
            # Update the json file
                with open(os.path.join(DATA_SRC, js), 'w') as f:
                    json.dump(data, f)

            pbar.update(1)
# Geocoding an address
# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
# print(geocode_result)
