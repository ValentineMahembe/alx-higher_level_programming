#!/bin/bash
# send a DELETE request to the URL passed as the first argument and show the body of the response
curl -sX DELETE "$1"
