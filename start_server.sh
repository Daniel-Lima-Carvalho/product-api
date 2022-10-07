#!/bin/bash

cd /home/ubuntu/product-api
source venv/bin/activate
gunicorn product_api.wsgi -b 0.0.0.0:8000
