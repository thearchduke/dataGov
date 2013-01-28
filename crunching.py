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
fout.write('<!DOCTYPE html><html><head><title>Word cloud for data.gov</title></head><body><div style="width: 800px;">')

divisor = float(top100[99][0])

#random.shuffle(top100)
top100.sort()

for pair in top100:
	size = pair[0] / divisor * 5
	fout.write("<span style='font-size: %spx;'>%s</span>  " % (size, pair[1]))

fout.write('</div></body></html>')

"""
####### now we make it pretty
def is_inside(test, boxes):
	for box in boxes:
		if test[0] > box[0] and test[2] < box[2]:
			if test[1] > box[1] and test[3] < box[3]:
				return True
	return False

boxes = []
for pair in top100:
	size = pair[0] / divisor * 5
	init_x = random.randint(1, 600)
	init_y = random.randint(1, 600)
	test_box = (init_x, init_y, init_x + len(pair[1]) * size, init_y + size)
	while is_inside(test_box, boxes):
		new_x = random.randint(1, 600)
		new_y = random.randint(1, 600)
		test_box = (new_x, new_y, new_x + len(pair[1]) * size, new_y + size)
	boxes.append(test_box)
	fout.write("<div style='font-size: %spx; left: %spx; top: %spx; position: absolute;'>%s</div>  " % (size, test_box[0], test_box[1], pair[1]))
"""

fout.write('</div></body></html>')
fout.close()

keyw.close()
descrip.close()
