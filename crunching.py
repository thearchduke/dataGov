import random

####### Open the keyword and description files
keyw = open('keywords.txt', 'r')
descrip = open('descriptions.txt', 'r')


####### Initialize the histogram arrays
keyw_dict = {}
descrip_dict = {}
boring = ['a', 'an', 'the', 'and', 'of', 'to', 'is', 'in', 'as', 'on', 'for',\
	'with', 'are', 'this', 'on', 'by', 'data', 'tri', 'http://www.epa.gov/tri/', "tri's",\
	'it', 'which', 'from', 'at', 'http://www.epa.gov/tri/.', 'r', '(tri)']


####### Histogram basics:
for line in keyw:
	for word in line.split():
		realWord = word.strip(',').lower()
		if realWord in keyw_dict and realWord not in boring:
			keyw_dict[realWord] += 1
		else:
			keyw_dict[realWord] = 1

for line in descrip:
	for word in line.split():
		realWord = word.strip(',').lower()
		if realWord in keyw_dict and realWord not in boring:
			keyw_dict[realWord] += 1
		else:
			keyw_dict[realWord] = 1



####### iteritems() here is important.
####### Anyway, this selects the top 100.

top100 = []
for key, value in sorted(keyw_dict.iteritems(), key=lambda (k,v): (v,k)):
	top100.append((value, key))

top100 = sorted(top100, reverse = True)[0:100]



####### produce display html

fout = open('cloud.html', 'w')
fout.write('<!DOCTYPE html><html><head><title>Word cloud for data.gov</title></head><body><div style="width: 600px;">')

divisor = float(top100[99][0])

random.shuffle(top100)

for pair in top100:
	size = pair[0] / divisor * 5
	fout.write("<span style='font-size: %spx;'>%s</span>  " % (size, pair[1]))

fout.write('</div></body></html>')
fout.close()


keyw.close()
descrip.close()
