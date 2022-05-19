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



''' now let's combine them somehow '''
import utils
import pandas as pd

idf = infinity77.load_df()
sdf = sfu.load_df()
bdf = benchmarkfcns.load_df()

i2s, _, _ = utils.diff_map(idf.name, sdf.name)
i2b, _, _ = utils.diff_map(idf.name, bdf.name)
b2s, _, _ = utils.diff_map(bdf.name, sdf.name)

i2s = dict(sorted(i2s.items(), key=lambda kv: kv[0]))
i2b = dict(sorted(i2b.items(), key=lambda kv: kv[0]))
b2s = dict(sorted(b2s.items(), key=lambda kv: kv[0]))


# first, all items that agree in all 3 should be taken
alist = []
for i, b in i2b.items():
    s_from_i = i2s.get(i)
    s_from_b = b2s.get(b)
    if s_from_i is None or s_from_b is None:
        continue
    if s_from_i == s_from_b:
        alist.append((i, b, s_from_i))

''' got input from user
newlist = []
for item in alist:
    print(item)
    y = input()
    newlist.append((y, *item))
'''
newlist = [
    ('', 'Ackley', 'Ackley', 'Ackley'),
    ('', 'Beale', 'Beale', 'Beale'),
    ('', 'Bohachevsky', 'Bohachevsky N. 1', 'Bohachevsky Functions'),
    ('n', 'BoxBetts', 'Booth', 'Booth'),
    ('', 'Cross-in-Tray', 'Cross-in-Tray', 'Cross-in-Tray'),
    ('', 'DropWave', 'Drop-Wave', 'Drop-Wave'),
    ('', 'Easom', 'Easom', 'Easom'),
    ('', 'Goldstein-Price', 'Goldstein-Price', 'Goldstein-Price'),
    ('', 'Griewank', 'Griewank', 'Griewank'),
    ('', 'HolderTable', 'Holder-Table', 'Holder Table'),
    ('', 'Matyas', 'Matyas', 'Matyas'),
    ('', 'McCormick', 'McCormick', 'McCormick'),
    ('n', 'Odd Square', 'Sum Squares', 'Sum Squares'),
    ('', 'Rastrigin', 'Rastrigin', 'Rastrigin'),
    ('', 'Rosenbrock', 'Rosenbrock', 'Rosenbrock'),
    ('', 'Schaffer 4', 'Schaffer N. 4', 'Schaffer Function N. 4'),
    ('', 'Schwefel 1', 'Schwefel', 'Schwefel'),
    ('', 'Sphere', 'Sphere', 'Sphere'),
    ('', 'StyblinskiTang', 'Styblinski-Tank', 'Styblinski-Tang'),
    ('', 'Three Hump Camel', 'Three-Hump Camel', 'Three-Hump Camel'),
    ('n', 'Wayburn and Seader 1', 'Gramacy & Lee', 'Gramacy & Lee (2012)'),
    ('', 'Zacharov', 'Zakharov', 'Zakharov'),
]
df3 = pd.DataFrame(newlist, columns=['yn', 'i', 'b', 's'])
df3 = df3[df3.yn == '']
for index, row in df3.iterrows():
    del i2s[row['i']]
    del i2b[row['i']]
    del b2s[row['b']]

# now we will look at sets of 2 individually

def remove_v(val, k2v):
    if val in k2v.values():
        for k, v in k2v.items():
            if v == val:
                del k2v[k]
                return

'''
alist = []
for i, s in i2s.items():
    print(i, '|', s)
    y = input()
    alist.append((y, i, s))
'''
alist = [
    ('n', 'BoxBetts', 'Booth'),
    ('', 'Branin 1', 'Branin'),
    ('', 'Colville', 'Colville'),
    ('', 'Dixon and Price', 'Dixon-Price'),
    ('', 'Egg Holder', 'Eggholder'),
    ('', 'Langermann', 'Langermann'),
    ('n', 'Levy 3', 'Levy'),
    ('', 'Michalewicz', 'Michalewicz'),
    ('n', 'Odd Square', 'Sum Squares'),
    ('n', 'PermFunction 1', 'Perm Function d, Beta'),
    ('', 'Powell', 'Powell'),
    ('', 'Power sum', 'Power Sum'),
    ('n', 'Rotated Ellipse 1', 'Rotated Hyper-Ellipsoid'),
    ('n', 'Shekel 5', 'Shekel'),
    ('', 'Shubert 1', 'Shubert'),
    ('', 'Six Hump Camel', 'Six-Hump Camel'),
    ('', 'Trid', 'Trid'),
    ('n', 'Wayburn and Seader 1', 'Gramacy & Lee (2012)'),
]
df_i2s = pd.DataFrame(alist, columns=['yn', 'i', 's'])
df_i2s = df_i2s[df_i2s.yn == '']
for index, row in df_i2s.iterrows():
    if row['i'] in i2s:
        del i2s[row['i']]
    if row['i'] in i2b:
        del i2b[row['i']]
    remove_v(row.s, b2s)

'''
alist = []
for i, b in i2b.items():
    print(i, '|', b)
    y = input()
    alist.append((y, i, b))
'''
alist = [
    ('', 'Adjiman', 'Adjiman'),
    ('', 'Alpine 1', 'Alpine N. 1'),
    ('', 'Alpine 2', 'Alpine N. 2'),
    ('', 'Bartels-Conn', 'Bartels Conn'),
    ('', 'Bird', 'Bird'),
    ('n', 'BoxBetts', 'Booth'),
    ('', 'Brent', 'Brent'),
    ('', 'Brown', 'Brown'),
    ('', 'Bukin 6', 'Bukin N. 6'),
    ('', 'Deckkers-Aarts', 'Deckkers-Aarts'),
    ('', 'Egg Crate', 'Egg Crate'),
    ('', 'Exponential', 'Exponential'),
    ('', 'HimmelBlau', 'Himmelblau'),
    ('n', 'Judge', 'Ridge'),
    ('', 'Keane', 'Keane'),
    ('', 'Leon', 'Leon'),
    ('n', 'Levy 3', 'Levi N. 13'),
    ('n', 'Odd Square', 'Sum Squares'),
    ('', 'Qing', 'Qing'),
    ('n', 'Quadratic', 'Quartic'),
    ('', 'Salomon', 'Salomon'),
    ('', 'Schaffer 1', 'Schaffer N. 1'),
    ('', 'Schaffer 2', 'Schaffer N. 2'),
    ('', 'Schaffer 3', 'Schaffer N. 3'),
    ('', 'Schwefel 20', 'Schwefel 2.20'),
    ('', 'Schwefel 21', 'Schwefel 2.21'),
    ('', 'Shubert 3', 'Shubert 3'),
    ('n', 'Tripod', 'Periodic'),
    ('n', 'Wayburn and Seader 1', 'Gramacy & Lee'),
    ('', 'Wolfe', 'Wolfe'),
    ('', 'Xin-She Yang 1', 'Xin-She Yang'),
]
df_i2b = pd.DataFrame(alist, columns=['yn', 'i', 'b'])
df_i2b = df_i2b[df_i2b.yn == '']
for index, row in df_i2b.iterrows():
    if row['i'] in i2b:
        del i2b[row['i']]
    if row['i'] in i2s:
        del i2s[row['i']]
    if row['b'] in b2s:
        del b2s[row['b']]


'''
alist = []
for b, s in b2s.items():
    print(b, '|', s)
    y = input()
    alist.append((y, b, s))
'''
alist = [
    ('', 'Booth', 'Booth'),
    ('', 'Gramacy & Lee', 'Gramacy & Lee (2012)'),
    ('', 'Levi N. 13', 'Levy Function N. 13'),
    ('', 'Sum Squares', 'Sum Squares'),
]
df_b2s = pd.DataFrame(alist, columns=['yn', 'b', 's'])
df_b2s = df_b2s[df_b2s.yn == '']
for index, row in df_b2s.iterrows():
    if row['b'] in b2s:
        del b2s[row['b']]
    remove_v(row.b, i2b)
    remove_v(row.s, i2s)


# the rest isn't worth it.
# now just build the data
# for index, row in df3.items():
#     idf[idf['i'] == row['i']].to_dict()

print(df3)

print(df_b2s)
print(df_i2b)
print(df_i2s)

print(i2s)
print(i2b)
print(b2s)

# sdf
# bdf

# TODO: add links to each row in dataframe so that we can add them to the links
# TODO: parse benchmarkfcns files
# TODO: combine cleanest data
# TODO: generate official database
# TODO: create notebooks showcasing examples of how to use database
# TODO: consider whether we should even use indusmic
# TODO: consider how the paper can be used

'''
@thieu1995 

Questions regarding some fields of benchmark methods


- Is Exponential Unimodal or Multi-modal? 
  - I believe it should be Uni-modal since it has one global minima
  - but the paper https://arxiv.org/pdf/1308.4008.pdf says it is multi-modal.


- Is Griewank Unimodal or Multimodal? 
  - https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/blob/gh-pages/benchmarkfcns/griewankfcn.markdown says uni-modal, 
  - the paper https://arxiv.org/pdf/1308.4008.pdf says multimodal. 
  - https://github.com/AxelThevenot/Python_Benchmark_Test_Optimization_Function_Single_Objective/blob/91c37d9d0f1f3366064004fdb3dd23e5c2681712/pybenchfunction/function.py#L1160 says it is unimodal. 
  - Looking at the image at http://infinity77.net/global_optimization/test_functions_nd_G.html#go_benchmark.Griewank, there are many minima, but there is a single best minima. I'm assuming it is multi-modal for now
  
- What is the x-value for the minima of mishra 1? References:
  - http://infinity77.net/global_optimization/test_functions_nd_M.html#go_benchmark.Mishra01
  - https://arxiv.org/pdf/1308.4008.pdf
  
- 
'''