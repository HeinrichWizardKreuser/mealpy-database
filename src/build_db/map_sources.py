from opfunu.dimension_based import benchmark1d, benchmark2d, benchmark3d, benchmarknd
from opfunu.type_based import multi_modal, uni_modal
import inspect

import pandas as pd
import utils
from scrapers import collector

ASSETS = '../assets/build_db'

def cls2name(cls):
    module = cls.Functions.__module__
    name = module.split('.')[-1]
    return name

def cls2methods(cls):
    return list(dict(inspect.getmembers(cls.Functions, predicate=inspect.isfunction)).keys())

def build_cls_df(classes):
    rows = []
    for cls in classes:
        name = cls2name(cls)
        methods = cls2methods(cls)
        for method_name in methods:
            clean_name = method_name.replace('_', ' ').strip()
            clean_name = ' '.join([ cn.capitalize() for cn in clean_name.split(' ') ])
            rows.append(dict(
                #cls=name,
                name=clean_name,
                #method=method_name,
                call=f'{name}.Functions().{method_name}',
            ))
    df = pd.DataFrame(rows)
    df = df.sort_values('name')
    df = df.reset_index(drop=True)
    return df


def build_df():
    # load the dataframes of the collected data
    source2df = {
        name: package.load_df()
        for name, package in collector.source2package.items()
    }

    # Load opfunu functions
    classes = [
        benchmark1d, benchmark2d, benchmark3d, benchmarknd, # total methods = 62
        # multi_modal, uni_modal, # total methods = 47
    ]
    df = build_cls_df(classes)

    # Map opfunu benchmarks to sources
    for source_id, source_df in source2df.items():
        # create mapping df
        source_map, *_ = utils.diff_map(df.name, source_df.name)
        source_map_df = pd.DataFrame(source_map.items(), columns=['name', source_id])
        # merge
        df = pd.merge(left=df, right=source_map_df, on='name', how='outer')

    df.to_csv(f'{ASSETS}/df.csv', index=False)
    return df
