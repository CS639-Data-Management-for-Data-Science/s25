import os
import json
from tqdm import tqdm

BASE = "./jsons"

dict_json = {"places": []}
with open("./jsons/places.json", "r") as f:
    lines = f.readlines()
    for k in lines:
        if "index" in k:
            continue
        ans = json.loads(k)
        ans["coordinates"] = f"{str(ans['coordinates'][0])} , {str(ans['coordinates'][1])}"
        dict_json["places"].append(ans)


with open("./jsons/locs.json", "w") as f:
    json.dump(dict_json, f)


# "wiki": "The State Street Halloween Party was an annual Halloween festival located in Madison, Wisconsin. Tens of thousands of party-goers, many dressed in Halloween costumes, attended the event on State Street in the downtown area of Madison. Most attendees were students from the University of Wisconsin–Madison and their guests, but others came from across Wisconsin and elsewhere. The city took control of the event in 2006, renaming it Freakfest and began charging admission. Prior to this, the event saw crowds of up to 100,000 and a plethora of riotous behavior. Freakfest was cancelled in 2020 and 2021 due to concerns related to the COVID-19 pandemic.\nIn 2022, the event was cancelled due to lack of funding and support. It did not return in 2023. However, State Street, a popular nightlife destination, saw an marked increase in crowds on Halloween weekend, requiring the Madison Police Department to have a larger than normal presence in the area.\nHistory\nIn 1977, a group of UW Madison students started a block party on Halloween night. Due to its growing popularity, the student government began to sponsor the event as a fundraiser in 1979. However, when the legal drinking age changed in 1986, the fundraising ceased as their primary money-making source was gone, leading to the eventual end of student government's sponsorship. From 1989 until the late 1990s, crowd size varied. By the 2000s, the event's size grew significantly and largely culminated in rioting resulting in vandalism, theft, property damage, arson, and assault; resulting in hundreds of arrests costing the city thousands of dollars. By 2003, the event became a point of contention in local government and was costing the city over $700,000. The cost of additional police, the potential of damage to local businesses, and the protection of the city's reputation prompted the concern of Madison leaders, some of whom suggested canceling the event altogether. In 2005, riot police used tear gas to disperse the riotous crowd of 100,000 and over 400 arrests occurred. In the summer of 2006, then-Mayor Dave Cieslewicz unveiled the city's plan for the upcoming Halloween events. The plan consisted of blocking off State Street, charging admission from select points of entry, and closing off the street at midnight. As a result, the riotous behavior ceased as the event became a largely peaceful festival. In 2006, the city government officially named the event Freakfest. The festival included films and live performances by nationally known musical artists with sponsors such as Mountain Dew. Alcohol possession and consumption on the street were prohibited but local bars and restaurants served Freakfest attendees.",