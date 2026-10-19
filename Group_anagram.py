from collections import defaultdict

def groupAnagrams(strs):

 d = defaultdict(list)

 for s in strs:

  d[tuple(sorted(s))).append(s)

 return list(d.values())
