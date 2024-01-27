#!/bin/bash
# Get request with header value
curl -X GET -H "X-School-User-Id: 98" -s "$1"
