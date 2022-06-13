import pandas as pd
from collections import defaultdict
import re

from scrapers import collector

source_ids = list(collector.source2package.keys())

source2df = collector.load_source2df()

ASSETS = '../assets/build_db'


# dict utils
def sort_dict(adict):
    return dict(sorted(adict.items(), key=lambda kv: kv[0]))

def set_and_get(f2v, f, v=None):
    f2v.setdefault(f, v)
    return f2v[f]

# general utils for building db
def crossref(source_id, name):
    source_df = source2df[source_id]
    row = source_df[source_df['name'] == name].iloc[0]
    return row.to_dict()

def frow(row):
    # collect each field-value(s) pairs for each source mentioned
    
    # first check whether this
    field2value = defaultdict(list)
    for source_id in source_ids:
        if not pd.isna(row[source_id]):
            # then this source exists for this source
            # cross reference its value to get dict of values
            adict = crossref(source_id, row[source_id])
            # print(adict)
            for field, value in adict.items():
                field2value[field].append(value)
    # add method
    field2value['method'] = row['call']
    
    field2value = sort_dict(field2value)
    return field2value


# general utils for building db
def wrap(s, r=''):
    if isinstance(s, list):
        return [ wrap(si) for si in s ]
    elif isinstance(s, str):
        return f'{r}"{s}"'

def wrapr(s):
    return wrap(s, r='r')

def handle_dimensions(f2v):    
    v = f2v.get('dimensions')
    if v is None:
        f2v['dimensions'] = wrap('TODO')
    else:
        v = v[0]
        if v.isdigit():
            f2v['dimensions'] = v
        else:
            f2v['dimensions'] = wrap(v)

            
def clean_np(item):
    if isinstance(item, list):
        item = [
            clean_np(i)
            for i in item
        ]
        return item
    matches = re.findall('((\d)np)', item)
    if matches:
        full, digit = matches[0]
        item = item.replace(digit, f'{digit}*')

    if ',' not in item:
        item = ', '.join(item.split(' '))
    
    return item
            
def handle_domain(f2v):
    v = set_and_get(f2v, 'domain')
    if v is not None:
        if len(set(v)) == 1:
            f2v['domain'] = clean_np(v[0])
        else:
            f2v['domain'] = [clean_np(vi) for vi in v]

def latex_treatment(f2v, f):
    v = set_and_get(f2v, f)
    if isinstance(v, list):
        v = [ wrapr(iv).replace('\n', '\\n') for iv in v ]
        if len(v) == 1:
            f2v[f] = v[0]
        else:
            f2v[f] = v
        
def handle_minima(f2v):
    v = set_and_get(f2v, 'minima')
    if v is not None:
        if len(v) == 1:
            v = v[0]
            v = eval(v)
            v = [ [ vii.strip() for vii in vi.split('=') ] for vi in v ]
            a = []
            for vk, vv in v:
                try:
                    eval(vv)
                except SyntaxError as se:
                    vv = wrapr(vv)
                a.append(f'{wrapr(vk)}: {vv}')
            v = '{' + ', '.join(a) + '}'
        f2v['minima'] = v

def handle_references(f2v):
    v = set_and_get(f2v, 'references')
    if v is None:
        return
    # combine the references (list of list)
    references = []
    for vi in v:
        alist = eval(vi)
        alist = [
            item.replace('"', '\\"')
            for item in alist
        ]
        alist = [
            item.replace('\n', '\\n')
            for item in alist
        ]
        alist = list(map(wrap, alist))
        references += alist
    f2v['references'] = tuple(references)
    


KNOWN_TAGS = [
    ('separable', 'non-separable'),
    ('continuous', 'discontinuous'),
    ('differentiable', 'non-differentiable'),
    ('multimodal', 'unimodal'),
    ('convex', 'non-convex'),
    ('scalable', 'non-scalable'),
    ('random', 'non-random'),
    ('parametric', 'non-parametric'),
]
def tags2dict(*tags):
    df = pd.DataFrame(KNOWN_TAGS, columns=['pos', 'neg'])
    adict = {}
    # clean tags
    tags = {
        tag.strip(',')
        for tag in tags
    }
    # iterate over each known tag
    for index, row in df.iterrows():
        # check if pos is present
        if row.pos in tags:
            tags.remove(row.pos)
            adict[row.pos] = True
            continue
        # check for negative
        if row.neg in tags:
            tags.remove(row.neg)
            adict[row.pos] = False
            continue
        # else nonw exists for this tag, set it to False
        adict[row.pos] = False
    # now check for any leftovers
    if tags:
        dimension, tags = dimensional(*tags)
        if dimension:
            adict['dimensions'] = dimension
    if tags:
        raise ValueError(f'Unrecognized tags: {tags}')
    return adict

def dimensional(*tags):
    for i, tag in enumerate(tags):
        if tag.endswith('-dimensional'):
            return tag.removesuffix('-dimensional'), tags[:i] + tags[i+1:]
    return None, tags 

def handle_tags(f2v):
    # sort before adding tags
    tags = f2v.get('tags')
    if tags is not None:
        del f2v['tags']
    f2v = sort_dict(f2v)
    
    # tags
    if tags is None:
        #f2v['tags'] = "TODO"
        return f2v, "TODO"
    
    try:
        tags = eval(tags[0])
    except Exception:
        #f2v['tags'] = "TODO"
        return f2v, "TODO"
 
    tags = tags2dict(*tags)
    # replace dimensions if it exists
    tdim = tags.get('dimensions')
    if tdim is not None:
        del tags['dimensions']
        fdim = f2v.get('dimensions')
        if fdim == '"TODO"':
            if tdim == 'n':
                tdim = wrap('*')
            f2v['dimensions'] = tdim
        else:
            # don't update if they are both n/d or equal
            if fdim == '"d"' and tdim == 'n':
                f2v['dimensions'] = wrap('*')
            elif fdim == tdim:
                pass
            else:
                f2v['dimensions'] = [fdim, tdim]

    #f2v.update(tags)

    return f2v, tags



def clean_field2value(f2v):
    ''' assert that dict contains a value for each field '''
    # dimensions
    handle_dimensions(f2v)

    # domain
    handle_domain(f2v)
    
    # domain_latex
    latex_treatment(f2v, 'domain_latex')

    # latex
    latex_treatment(f2v, 'latex')
    
    # links
    links = f2v['link']
    del f2v['link']
    f2v['links'] = tuple(wrap(links))
    
    # method
    f2v['method'] # throws a KeyError if not present
    
    # minima
    handle_minima(f2v)

    # minima_latex
    latex_treatment(f2v, 'minima_latex')
    
    # name
    names = list(sorted(set(f2v['name'])))
    if len(names) == 1:
        f2v['name'] = wrap(names[0])
    else:
        f2v['name'] = wrap(names)
    
    # references
    handle_references(f2v)
    
    # tags
    # TODO: figure out a way to have a comment '#tags' before tags is printed
    f2v = handle_tags(f2v)
    
    return f2v


def build_db(filepath=f'{ASSETS}/db.py', keep=True):
    df = pd.read_csv(f'{ASSETS}/df.csv')
    
    s = ''
    # add imports
    s += 'from opfunu.dimension_based import benchmark1d, benchmark2d, benchmark3d, benchmarknd\n'
    s += 'import numpy as np\n'
    s += '\n'
    s += 'data = [\n'
    t = '    '
    for index, row in df.iterrows():
        field2value = frow(row)
        field2value, tags = clean_field2value(field2value)
        # if keep, skip tags if incomplete
        if not keep:
            if isinstance(tags, str):
                continue
        # add name
        s += f"{t}# {row['name']}\n{t}dict(\n"
        # first add normal field and values
        for field, values in field2value.items():
            s += f"{t*2}{field}="
            if isinstance(values, list):
                if keep:
                    s += f'\n{t*3}'
                    s += f',\n{t*3}'.join(values)
                else:
                    s += values[0]
            elif isinstance(values, tuple):
                s += f'[\n{t*3}'
                s += f',\n{t*3}'.join(values)
                s += f',\n{t*2}]'
            elif values is None:
                s += 'None'
            else:
                s += values
            s += f',\n'
        # add tags
        s += f'{t*2}# tags\n'
        if isinstance(tags, str):
            s += f'{t*2}# TODO\n'
        else:
            for field, value in tags.items():
                s += f"{t*2}{field}={value},\n"
        s += f'{t}),\n'
    s += ']'
    # write
    with open(filepath, 'w') as f:
        f.write(s)
	# print(s)


def main():
	# build_db(keep=True)
	build_db(filepath='trial/db.py', keep=False)

if __name__ == '__main__':
	main()

