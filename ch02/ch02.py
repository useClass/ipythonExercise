#-*- coding:GB2312 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



import json

path='D:\pydata-book-master\ch02\usagov_bitly_data2012-03-16-1331923249.txt'

records = [json.loads(line) for line in open(path)]

time_zones = [rec['tz'] for rec in records if 'tz' in rec]

#print records[0]['tz']

def get_counts(sequence):
	counts = {}
	for x in sequence:
		if x in counts:
			counts[x] += 1
		else:
			counts[x] = 1
	return counts


from collections import defaultdict
def get_counts2(sequence):
	counts = defaultdict(int)
	for x in sequence:
		counts[x] += 1
	return counts

counts = get_counts(time_zones)
#print counts['America/New_York']
print "区域的总个数为："
print len(time_zones)


print "前十个区域分别为："
def top_counts(count_dict, n=10):
	value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
	value_key_pairs.sort()
	return value_key_pairs[-n:]
	
#print top_counts(counts)

from collections import Counter
counts = Counter(time_zones)
#print counts.most_common(10)


from pandas import DataFrame,Series
import pandas as pd; import numpy as np
frame = DataFrame(records)
#print frame
print frame['tz'][:10]

tz_counts = frame['tz'].value_counts()

print '前十区域名字与数量'
print tz_counts[:10]
tz_counts[:10].plot(kind='barh',rot=0)
#plt.show()

results = Series([x.split()[0] for x in frame.a.dropna()])

print results[:5]


print results.value_counts()[:8]

cframe = frame[frame.a.notnull()]
operating_system = np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')
print 'Windows用户统计:'
#print operating_system[:5]
by_tz_os = cframe.groupby(['tz',operating_system])
agg_counts = by_tz_os.size().unstack().fillna(0)
print agg_counts[:10]

print '最常见的时区：'
indexer = agg_counts.sum(1).argsort()
print indexer[:10]

count_subset = agg_counts.take(indexer)[-10:]
print count_subset

count_subset.plot(kind='barh', stacked=True)

normed_subset = count_subset.div(count_subset.sum(1), axis=0)
normed_subset.plot(kind='barh', stacked=True)

plt.show()



























































































