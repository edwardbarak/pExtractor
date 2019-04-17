#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup as bs

def extract(url, elementClass=None):
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    # selection = soup.find_all(selector)

presets = {'p': ''}
