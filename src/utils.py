import difflib

def diff_map(a, b):
    """ Creates mapping for each word in a to each word in b.

    Reamining words that could not be matches are sent back.

    Args:
        a: list of strings to map to words in b
        b: list of strings

    Returns:
        dictionary containing the mapped words under 'mapping' as well as the
        words that were unable to be mapped with a list of their close matches.
        example:
        
        {
            mapping: {str in a --matching--> str in b},
            a2bestmatches: [],
            b2bestmatches: []
        }
    """
    a, b = a.copy(), b.copy()
    
    # create matrix of a to b, with ratios as the items (vice versa for b to a)
    a2matches = {
        ai: {
            bi: difflib.SequenceMatcher(None, ai, bi).ratio() 
            for bi in b
        }
        for ai in a
    }
    
    b2matches = {
        bi: {
            ai: a2matches[ai][bi]
            for ai in a
        }
        for bi in b
    }
    # for each item in a and b, list matches in order of highest ratio
    a2bestmatches = {
        a: sorted(matches, key=matches.get, reverse=True)
        for a, matches in a2matches.items()
    }
    b2bestmatches = {
        b: sorted(matches, key=matches.get, reverse=True)
        for b, matches in b2matches.items()
    }

    # map each word if we can
    a2b = {}
    nomatch = []
    for a, bestmatches in a2bestmatches.items():
        bestmatch = bestmatches[0]
        
        other_bestmatch = b2bestmatches[bestmatch][0]
        if a == other_bestmatch:
            a2b[a] = bestmatch
        else:
            nomatch.append(a)
    
    # get what remains after the matching
    for a, b in a2b.items():
        del a2bestmatches[a]
        del b2bestmatches[b]
    for a, bestmatches in a2bestmatches.items():
        a2bestmatches[a] = list(filter(
            lambda bestmatch: bestmatch in b2bestmatches, 
            bestmatches)
        )
    for b, bestmatches in b2bestmatches.items():
        b2bestmatches[b] = list(filter(
            lambda bestmatch: bestmatch in a2bestmatches, bestmatches)
        )
    
    return a2b, a2bestmatches, b2bestmatches


import json
def jprint(obj):
    print(json.dumps(obj, indent=4, sort_keys=True))
