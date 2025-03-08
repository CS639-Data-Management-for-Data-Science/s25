import google_streetview.api
import os
from tqdm import tqdm
import json

DATA_SRC = "/home/agarg54/p4_cs639/data/jsons"
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
                    # print(geocode_result)
                    params = [{
                        'size': '128x128', 
                        'location': place["formattedAddress"],
                        'key': 'gm_img_key',
                        'fov': '120'}]
                    res = google_streetview.api.results(params)
                    res.download_links(f"/home/agarg54/p4_cs639/data/images/downloads_{js.split('.')[0]}/{place['displayName']['text']}")

            # with open(os.path.join(DATA_SRC, js), 'w') as f:
            #     json.dump(data, f)
        pbar.update(1)
