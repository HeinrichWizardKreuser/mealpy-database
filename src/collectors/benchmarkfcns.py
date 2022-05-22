'''
1. Download the github code
    https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/tree/gh-pages/benchmarkfcns
2. For each markdown file
    - name (title)
    - tags
    - latex
    - plots?
    - input domain
    - global minima
    - references
'''

import glob
import pandas as pd
from collectors import utils

ASSETS = '../assets/benchmarkfcns'
PAGES_PATH = f'{ASSETS}/markdown'

BASE_URL = 'https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns'

def crawl_markdown():
    filepaths = sorted(glob.glob(f'{PAGES_PATH}/*.markdown'))
    rows = []
    for filepath in filepaths:
        with open(filepath, 'r') as f:
            lines = f.read()
        adict = collect(lines.split('\n'))
        row = extract(filepath, adict)
        rows.append(row)
    df = pd.DataFrame(rows)
    df.to_csv(f'{ASSETS}/df.csv', index=False)


def extract(filepath, adict):
    try:
        latex = adict['Mathematical Definition'][1]
    except KeyError as e:
        utils.jprint(adict)
        raise e

    refs = []
    ref = ''
    for line in adict['References']:
        if line.startswith('*'):
            if ref != '':
                refs.append(ref)
            ref = line[1:].strip()
        else:
            ref += (' ' + line.strip())
    refs.append(ref)
    refs = [
        ref[1:ref.find(']')]
        for ref in refs
    ]

    name = adict['summary']['title']
    name = name.removesuffix(' Function')

    tags = adict['summary']['tags'].split(' ')

    # keep the minima as is since it should be described in detail
    minima_latex = adict['Global Minima'][0]
    # if 'one' in minima or 'The global' in minima:
    #     minima = minima[minima.find('$'):]
    
    # split the domain up into python and latex
    domain = adict['Input Domain'][0]
    domain_latex = domain[domain.find('$'):]
    domain_latex = domain_latex.removesuffix('.')

    a, b = domain_latex.find('['), domain_latex.find(']')
    domain = domain_latex[a:b+1]
    domain = domain.replace(r'\pi', '*np.pi')
    
    # link
    href = filepath.removeprefix(PAGES_PATH)
    link = f'{BASE_URL}{href}'

    return dict(
        name=name,
        latex=latex,
        references=refs,
        tags=tags,
        domain=domain,
        domain_latex=domain_latex,
        minima_latex=minima_latex,
        link=link,
        )


'''
def clean_domain(domain: str):
    domain = domain \
        .removeprefix('The function can be defined on any ') \
        .removeprefix('positive ') \
        .removeprefix('input domain').removeprefix('.').removeprefix(' ') \
        .removeprefix('but ') \
        .removeprefix('it ').removeprefix('It ') \
        .removeprefix('is ') \
        .removeprefix('usually ') \
        .removeprefix('evaluated ') \
        .removeprefix('on ') \
        .removeprefix('the ') \
        .removeprefix('hypercube ')
    return domain
'''


def collect(lines: list[str]):
    adict = {}
    title = 'summary'
    alist = []
    for line in lines:
        if line == '':
            continue
        if line.startswith('# '):
            adict[title] = alist
            alist = []
            title = line.removeprefix('#').removesuffix(':').strip()
        else:
            alist.append(line)
    adict[title] = alist

    # update summary list
    summary = {}
    for line in adict['summary'][1:-1]:
        index = line.find(':')
        k, v = line[:index], line[index+1:]
        k, v = k.strip(), v.strip()
        summary[k] = v
    adict['summary'] = summary

    return adict


def load_df():
    df = pd.read_csv(f'{ASSETS}/df.csv')
    return df
