####### Open the keyword and description files
keyw = open('keywords.txt', 'r')
descrip = open('descriptions.txt', 'r')


####### Initialize the histogram arrays and the iterator
keyw_dict = {}
hist_dict = {}
#i = 0


####### Histogram basics:
for line in keyw:
	for word in line.split():
		realWord = word.strip(',')
		if realWord in keyw_dict:
			keyw_dict[realWord] += 1
		else:
			keyw_dict[realWord] = 1

size = len(keyw_dict)



####### iteritems() here is important.
####### Anyway, this selects the top 100.

top100 = []
for key, value in sorted(keyw_dict.iteritems(), key=lambda (k,v): (v,k)):
	top100.append((value, key))

top100 = sorted(top100, reverse = True)[0:99]

print top100

#	if value > 10000000.0 / size:
#		print key, value



keyw.close()
descrip.close()
