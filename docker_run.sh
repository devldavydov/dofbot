#!/bin/bash

TOKEN=$1
docker run -d --restart always dofbot $TOKEN
