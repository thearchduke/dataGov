import string

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



####### iteritems() here is GOOD and important. NOTE TO SELF: Figure out 
####### why.


size = len(keyw_dict)


####### Anyway, here comes the good stuff. Not really true. Come up with 
##### a good formula here. if value > etc. should be dependent upon len(etc.).
##### etc.
 
for key, value in keyw_dict.iteritems():
	if value > 10000000.0 / size:
		print key, value


'''
for line in descrip:
	for word in line.split():
		######## PRO TIP: Remember what's about to happen, it's awesome
		test = word.translate(string.maketrans("",""), string.punctuation)
		if test in keyw_dict:
			hist_dict[test] += 1
		else:
			hist_dict[test] = 1
'''


keyw.close()
descrip.close()
