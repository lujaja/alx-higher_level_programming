#!/usr/bin/bash
# Displaye the bode of 200 status code response
if [ -z "$1" ]; then
	exit 1
else
	url="$1"
fi

curl -sL "$url"
