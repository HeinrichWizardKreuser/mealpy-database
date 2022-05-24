from collectors import sfu, infinity77, benchmarkfcns


''' sfu '''
# sfu.download_homepage()
# sfu.download_functions()
sfu.crawl_functions()

''' infinity77 '''
# infinity77.download_homepage()
# infinity77.download_pages()
infinity77.crawl_pages()

''' benchmarkfcns '''
benchmarkfcns.crawl_markdown()

"""
Now that db file is complete, we want to take it for a test run.

We will first need to write a version of the db.py file that has a single value for each field instead of a list of values

Then we need to write a notebook where we show off the following

- Use the database to filter benchmarks that have a certain tag
- Select some algorithms from the mealpy library
- Run experiment(s) where each algorithm solves each of the selected 
    benchmarks while storing the results
- Programmatically plot results such that it is clear how each algorithm 
    performs on each benchmark such that the developer can conclude whether 
    an algorithm is more suited for landscapes of one tag or the other.

"""