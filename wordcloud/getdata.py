import urllib2, csv

def get_dataGov_csv():
	webFile = urllib2.urlopen('https://datagov.socrata.com/api/views/pyv4-fkgv/rows.csv?accessType=DOWNLOAD')
	fout = open('data/data.csv', 'w')
	fout.write(webFile.read())
	fout.close()

def make_txt():
	keyw = open('data/keywords.txt', 'w')
	descrip = open('data/descriptions.txt', 'w')

	with open('data/data.csv') as csvfile:
		converter = csv.reader(csvfile, delimiter=',')
		for row in converter:
			keyw.write(row[5])
			keyw.write(' ')
			descrip.write(row[3])
			descrip.write(' ')
		descrip.close()
		keyw.close()
