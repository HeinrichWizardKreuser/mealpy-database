import requests
from bs4 import BeautifulSoup
import json


def read_html(filepath):
    with open(filepath, 'r') as f:
        html = f.read()
    soup = BeautifulSoup(html, "html.parser")
    return soup


def write_html(html, filepath):
    with open(filepath, 'wb') as f:
        f.write(html)


def download_to(url, filepath):
    response = requests.get(url)
    html = response.content
    write_html(html, filepath)


def jprint(obj):
    print(json.dumps(obj, indent=4, sort_keys=True))
