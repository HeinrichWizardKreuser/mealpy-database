from scrapers import sfu, infinity77, benchmarkfcns


def crawl():
    ''' Crawl the online sources to download their HTML to local files 
        web --[crawl]--> local HTML '''
    # sfu
    sfu.download_homepage()
    sfu.download_functions()

    # infinity77
    infinity77.download_homepage()
    infinity77.download_pages()

    # benchmarkfcns
    # TODO: we already downloaded the github data
    pass



source2package = {
    'sfu': sfu,
    'infinity77': infinity77,
    'benchmarkfcns': benchmarkfcns,
}

def scrape():
    # TODO: add check to see whether we've a
    # crawl the methods to get the dataframes
    # return {
    #     name: package.crawl()
    #     for name, package in source2package.items()
    # }
    name2df = {}
    for name, package in source2package.items():
        df = package.crawl()
        name2df[name] = df
    return name2df


def load_source2df():
    return {
        name: package.load_df()
        for name, package in source2package.items()
    }