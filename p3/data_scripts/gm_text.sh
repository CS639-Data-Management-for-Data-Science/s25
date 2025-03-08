#!/bin/bash

curl -X POST -d '{
  "textQuery" : "Political buildings in Madison, Wisconsin"
}' \
    -H 'Content-Type: application/json' -H 'X-Goog-Api-Key: your-key' \
    -H 'X-Goog-FieldMask: places.displayName,places.formattedAddress,places.priceLevel' \
    'https://places.googleapis.com/v1/places:searchText' > political.json
