import re
from collections import Counter

c=Counter()
for eachline in open("query.log"):
    c.update(re.findall(r"client .*?query: (\S+)", eachline))

print(c.most_common(5))
