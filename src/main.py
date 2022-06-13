'''
web --[crawl]--> local HTML --[scrape]--> df.csv --[build-db]--> db.py
'''

from scrapers import collector
from build_db import compiler

"""
TODO: entries do not define whether they are scalable, fix this

Build a notebook that performs the following:
- Use the database to filter benchmarks that have a certain tag
- Select some algorithms from the mealpy library
- Run experiment(s) where each algorithm solves each of the selected 
    benchmarks while storing the results
- Programmatically plot results such that it is clear how each algorithm 
    performs on each benchmark such that the developer can conclude whether 
    an algorithm is more suited for landscapes of one tag or the other.

"""


def main():
    # scrapers_main.crawl()
    # name2df = scrapers_main.scrape()
    # build_db(name2df)

    compiler.main()

if __name__ == '__main__':
    main()