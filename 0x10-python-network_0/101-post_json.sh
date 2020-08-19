#!/bin/bash
# json 
curl -sH "Content-Type: application/json" "$1" -X POST -d @"$2"
