#!/usr/bin/bash
# Display all http methods the server will accept
curl -X OPTIONS -i -s "$1" | grep "Allow:" | awk '{print $2}'
