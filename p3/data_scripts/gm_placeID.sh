#!/bin/bash

curl -X GET -H 'Content-Type: application/json' \
    -H "X-Goog-Api-Key: your-key" \
    -H "X-Goog-FieldMask: id,displayName" \
    https://places.googleapis.com/v1/places/ChIJF4Yf2Ry7j4AR__1AkytDyAE
