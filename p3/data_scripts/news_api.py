#!/usr/bin/env python
import os
import requests
from newsapi import NewsApiClient
import json

newsapi = NewsApiClient(api_key='news-api-key')
madison_news = newsapi.get_everything(q='+Madison +Wisconsin -Elections -Harris -Kamala', 
                                      from_param="2024-09-08")
with open("/home/agarg54/p4_cs639/data/text/news_trump.json", "w") as f:
    json.dump(madison_news, f)
# with open("/home/agarg54/p4_cs639/data/text/news_madison.json", "w") as f:
#     json.dump(madison_news, f)
