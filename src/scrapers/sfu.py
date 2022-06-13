'''
1. Download the page
    https://www.sfu.ca/~ssurjano/optimization.html
2. Visit each function page, get data
    - name
    - dimension
    - references
    - domain

'''
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import glob
import pandas as pd
from scrapers import utils

import os

BASE_URL = 'https://www.sfu.ca/~ssurjano'
HOMEPAGE_URL = f'{BASE_URL}/optimization.html'
ASSETS = '../assets/sources/sfu'
HOMEPAGE_PATH = f'{ASSETS}/homepage.html'
FUNCTION_PATH = f'{ASSETS}/functions'


def download_homepage():
    utils.download_to(
        url=HOMEPAGE_URL,
        filepath=HOMEPAGE_PATH
    )


def download_functions():
    soup = utils.read_html(HOMEPAGE_PATH)
    items = soup.find_all('li')
    for item in tqdm(items):
        href = item.a.attrs['href']
        utils.download_to(
            url=f'{BASE_URL}/{href}',
            filepath=f'{FUNCTION_PATH}/{href}'
        )
        

def crawl_functions():
    html_paths = glob.glob(f'{FUNCTION_PATH}/*.html')
    data = []
    for html_path in html_paths:
        soup = utils.read_html(html_path)
        # name
        name = soup.find('div', {'id': 'name'}).text.strip()
        name = name.removesuffix(' Function')
        # get info to get the rest
        info = soup.find('div', {'id': 'info'})
        # dimension
        dimensions = info.find('i').text
        dimensions = dimensions.removeprefix('Dimensions: ')
        
        # references
        references = [
            ref.text
            for ref in info.find_all('p')
        ]
        
        # domain
        alist = info.text.split('\n')
        index = alist.index('Input Domain:')

        domain = alist[index+1]
        domain_latex = domain[domain.find('x'):]
        domain_latex = domain_latex.removesuffix('.')

        # link
        href = html_path.removeprefix(FUNCTION_PATH)
        link = f'{BASE_URL}{href}'

        data.append(dict(
            name=name,
            dimensions=dimensions,
            references=references,
            domain_latex=domain_latex,
            link=link,
        ))
    df = pd.DataFrame(data)
    df.to_csv(f'{ASSETS}/df.csv', index=False)
    return df


def crawl():
    return crawl_functions()

'''
def clean_domain(domain: str):
    domain = domain \
        .removeprefix('The ').removeprefix('This ') \
        .removeprefix('function ').removeprefix('functions ') \
        .removeprefix('are ') \
        .removeprefix('is ') \
        .removeprefix('usually ') \
        .removeprefix('evaluated ') \
        .removeprefix('on ') \
        .removeprefix('the ') \
        .removeprefix('square ').removeprefix('hypercube ').removeprefix('rectangle ')
    return domain
'''


def load_df():
    df = pd.read_csv(f'{ASSETS}/df.csv')
    return df
