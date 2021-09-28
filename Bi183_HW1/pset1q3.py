import numpy as np
from itertools import combinations

def probability_tree(labels, sequence):
    terms = []
    for l in labels: 
        tmp = []
        tmp.append("init({})*{}_{}".format(l, l, sequence[0]))
        terms.append(tmp.copy())
    for i in range(len(labels)): 
        for j in range(len(labels)):
            prob_help(labels, terms[i], labels[i], labels[j], sequence[1:], '')
    retstr = ''
    for t in terms: 
        retstr += "+ {}*(".format(t[0])
        for l in t[1:len(t)-1]: 
            retstr += l + " + "
        retstr += t[len(t)-1] + ") "
    print(retstr[2:])
    return terms

def prob_help(labels, terms, prev_state, curr_state, seq, prob): 
    if len(seq) == 1:
        prob += "*{}{}*{}_{}".format(prev_state, curr_state, curr_state, seq)
        terms.append(prob[1:])
    else:
        prob += "*{}{}*{}_{}".format(prev_state, curr_state, curr_state, seq[0])
        for i in range(len(labels)): 
            prob_help(labels, terms, curr_state, labels[i], seq[1:], prob)
        
print("P_111")
t111 = probability_tree(["A", "B"], "111")
print("P_000")
t000 = probability_tree(["A", "B"], "000")
print("P_110")
t110 = probability_tree(["A", "B"], "110")
print("P_011")
t011 = probability_tree(["A", "B"], "011")
print("P_100")
t100 = probability_tree(["A", "B"], "100")
print("P_001")
t001 = probability_tree(["A", "B"], "001")

A = ["A_0", "A_1"]
B = ["B_0", "B_1"]

tmp = t100.copy()
for t in tmp: 
    for str in range(len(t)): 
        if any(s in t[str] for s in A):
            t[str] = 0
print(tmp)

tmp = t001.copy()
for t in tmp: 
    for str in range(len(t)): 
        if any(s in t[str] for s in A):
            t[str] = 0
print(tmp)

p = ["AA", "AB", "BA", "BB", "A_0", "A_1", "B_0", "B_1"]
ts = [t111, t000, t110, t011, t110, t001]
comb = [list(combinations(p, i)) for i in range(len(p))]
#print(comb)
zero_combs000 = []
zero_combs111 = []
status = 0
for c in comb: 
    for i in c: 
        #tmp = [j for i in t000 for j in i]
        tmp = t000[1].copy()
        tmp = [e for e in tmp if "init" not in e]
        for t in range(len(tmp)): 
            if any(s in tmp[t] for s in i): 
                tmp[t] = 0
            if np.array_equal(np.asarray(tmp), np.zeros((1, len(tmp)))[0]): 
                zero_combs000.append(i)
        #tmp = [j for i in t111 for j in i]\
        tmp = t111[1].copy()
        #print(tmp)
        tmp = [e for e in tmp if "init" not in e]
        for t in range(len(tmp)): 
            if any(s in tmp[t] for s in i): 
                tmp[t] = 0
            if np.array_equal(np.asarray(tmp), np.zeros((1, len(tmp)))[0]): 
                zero_combs111.append(i)
print()
#print([i for i in list(set(zero_combs000) & set(zero_combs111)) if len(i) < 4])
#print(zero_combs000)
