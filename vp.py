from collections import Counter

def gini(ar):
    n = len(ar)
    counts = Counter(ar).values()
    ans = 0
    for c in counts:
        ans += (c / n) * (1 - c / n)
    return ans
print(gini([1, 1, 2, 2, 2, 3]))

'''def gini(sample_ans):
    sample_ans = 
    p = []
    s = set(sample_ans)
    for elem in s:
        p.append(sample_ans.count(elem) / len(sample_ans))
        print(p[-1])'''

print(gini([1, 1, 2, 2, 2, 3]))
