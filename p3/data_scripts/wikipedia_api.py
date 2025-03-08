#!/usr/bin/env python
import os
import requests
import json
import wikipediaapi
from tqdm import tqdm

DATA_SRC = "/home/agarg54/p4_cs639/data/jsons"
wiki_wiki = wikipediaapi.Wikipedia(
        user_agent='MyProjectName (emailid@gmail.com)',
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI)

p_wiki = wiki_wiki.page("Memorial Union (University of Wisconsin–Madison)")
with open("/home/agarg54/p4_cs639/data/text/wiki_memorial.txt", "w") as f:
    f.write(p_wiki.text)
