#!/usr/bin/bash
# Display size of body if response
if [ -z "$1" ]; then 
	exit 1
else
	url="$1"
fi

curl -s "$url" | wc -c
