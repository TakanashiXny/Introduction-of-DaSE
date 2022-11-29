with open(r'E:\学习\数据科学与工程导论\lab6\实验用.txt', "r", encoding='utf-8') as f:
    rl = f.readline()
    f.seek(0)
    rls = f.readlines()
print(rl)
print(rls)
