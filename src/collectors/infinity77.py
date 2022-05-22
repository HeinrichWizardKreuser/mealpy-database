'''
1. download html page of
    http://infinity77.net/global_optimization/test_functions.html

2. Go to each page in the index and download that page
3. For each downloaded page, get all data on each function:
    - name
    - latex function
    - x_i
    - global optimum
'''


import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import glob
import pandas as pd
from collectors import utils


BASE_URL = 'http://infinity77.net/global_optimization'
HOMEPAGE_URL = f'{BASE_URL}/test_functions.html'
ASSETS = '../assets/infinity77'
HOMEPAGE_PATH = f'{ASSETS}/homepage.html'
PAGES_PATH = f'{ASSETS}/pages'


def download_homepage():
    utils.download_to(
        url=HOMEPAGE_URL,
        filepath=HOMEPAGE_PATH
    )


def download_pages():
    soup = utils.read_html(HOMEPAGE_PATH)
    simples = soup.find_all('ul', {'class': 'simple'})
    simples = simples[1:-1]
    hrefs = []
    for simple in simples:
        href = simple.find('li').a.attrs['href']
        hrefs.append(href)
    for href in tqdm(hrefs):
        utils.download_to(
            url=f'{BASE_URL}/{href}',
            filepath=f'{PAGES_PATH}/{href}'
        )


def get_domain(p):
    for item in p[1:-1]:
        if '\in' in str(item):
            return item


def crawl_pages():
    data = []
    html_paths = glob.glob(f'{PAGES_PATH}/*')
    for html_path in html_paths:
        soup = utils.read_html(html_path)
        items = soup.find_all('dl', {'class': 'class'})
        for item in items:
            p = item.find_all('p')
            # name
            name = p[0].text
            name = name.removesuffix(' test objective function.')
            # latex
            latex = item.find('div', {'class': 'math'}).p.img.attrs['alt']
            # global optimum
            go = p[-1]

            # minima = ['f(x_i) = 0', 'x_i = 0', 'i=1,...,n']
            try:
                index = go.index(go.find('img'))
            except ValueError as ve:
                go = p[-2]
                index = go.index(go.find('img'))
            alts = list(go.children)[index:]
            minima_latex = ''
            minima = []
            for child in alts:
                if isinstance(child, str):
                    minima_latex += child.text
                else:
                    alt = child.attrs['alt'] 
                    minima.append(alt)
                    minima_latex += alt
            minima = minima[:2]

            # x_i
            domain = get_domain(p)
            if domain:
                domain = [ i.attrs['alt'] for i in domain.find_all('img') ]
                if len(domain) == 2 and domain[0] == 'n':
                    domain_latex = domain[1]
                elif len(domain) == 3:
                    domain_latex = f'{domain[1]}, {domain[2]}'
                else:
                    if domain[0] == 'n':
                        domain_latex = ', '.join(domain[1:])
                    else:
                        domain_latex = ', '.join(domain)
                domain = domain[1]
                a, b = domain.find('['), domain.find(']')
                domain = domain[a:b+1]
                domain = domain \
                    .replace(r'\pi', 'np.pi') \
                    .replace(r'\infty', 'np.inf')

            # link
            link = html_path.removeprefix(PAGES_PATH)
            link = link[:link.find('#')]
            href = item.find('a', {'class': 'headerlink'}).attrs['href']
            link = f'{BASE_URL}{link}{href}'

            adict = dict(
                name=name,
                latex=latex,
                minima=minima,
                minima_latex=minima_latex,
                domain=domain,
                domain_latex=domain_latex,
                link=link,
            )
            data.append(adict)
    df = pd.DataFrame(data)
    df.to_csv(f'{ASSETS}/df.csv', index=False)


def load_df():
    df = pd.read_csv(f'{ASSETS}/df.csv')
    return df