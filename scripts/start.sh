#!/bin/bash

cd /opt/paas-dashboard
python app.py
tail -f /dev/null
