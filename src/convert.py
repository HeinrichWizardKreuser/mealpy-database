
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
    tags = list(tags)
    adict = {}
    for i, (pos, neg) in enumerate(KNOWN_TAGS):
        if not tags:
            for pos, _ in KNOWN_TAGS[i:]:
                adict[pos] = False
            return adict
        elif pos in tags:
            adict[pos] = True
            tags.remove(pos)
        elif neg in tags:
            adict[pos] = False
            tags.remove(neg)
        else:
            adict[pos] = False
    if tags:
        dimension, tags = dimensional(*tags)
        if dimension:
            adict['dimension'] = dimension
    if tags:
        raise ValueError(f'Unrecognized tags: {tags}')
    return adict

def dimensional(*tags):
    for i, tag in enumerate(tags):
        if tag.endswith('-dimensional'):
            return tag.removesuffix('-dimensional'), tags[:i] + tags[i+1:]
    return None, tags 

import pprint
def format_tags(*tags):
    adict = tags2dict(*tags)
    result = pprint.pformat(adict, indent=4)
    result = convert(result) \
        .removeprefix('dict(') \
        .removesuffix(')')
    result = ' ' + result + ','
    return result


import re
def convert(s):
    return curly2dict(s)

_curly2dict_re = re.compile(r"""('\w+': )|("\w+": )""")
def curly2dict(curly: str):
    """ {'a': 0, 'b': 1} -> dict(a=0, b=1) """
    kwargs = _curly2kwargs(curly)
    adict = _kwargs2dict(kwargs)
    return adict
def _curly2kwargs(curly: str):
    """ {'a': 0, 'b': 1} -> a=0, b=1 """
    matches = [ m for m in _curly2dict_re.finditer(curly) ]
    kwargs = curly
    for m in matches[::-1]:
        a, b = m.span()
        kwargs = kwargs[:a] + f"{curly[a+1:b-3]}=" + kwargs[b:]
    return kwargs[1:-1]
def _kwargs2dict(s: str):
    """ a=0, b=1 -> dict(a=0, b=1) """
    return 'dict(' + s + ')'


