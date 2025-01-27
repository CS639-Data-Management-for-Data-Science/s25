#! /usr/bin/python3

import csv
from pathlib import Path
import time

count = 0

with open(Path("data") / Path("spotify.csv")) as FH:
    csv_file = csv.reader(FH)
    for line in csv_file:
        count += 1
        time.sleep(1) # sleep 1s

print(count)
