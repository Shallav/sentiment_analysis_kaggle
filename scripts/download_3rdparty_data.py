import os
import urllib2

import nltk

from samr.settings import DATA_PATH

# Create data folder if necessary
if not os.path.isdir(DATA_PATH):
    print("Creating data folder at {}".format(DATA_PATH))
    os.makedirs(DATA_PATH)
else:
    print("Data folder found at {}".format(DATA_PATH))

# Download inquirer data
filename = os.path.join(DATA_PATH, "inquirerbasicttabsclean")
url = "http://www.wjh.harvard.edu/~inquirer/inqtabs.txt"
if not os.path.isfile(filename) or os.stat(filename).st_size != 2906024:
	print("Downloading {} into {}".format(url, filename))


	u = urllib2.urlopen(url)
	f = open(filename, 'wb')
	meta = u.info()
	file_size = int(meta.getheaders("Content-Length")[0])
	print "Downloading: %s Bytes: %s" % (filename, file_size)

	file_size_dl = 0
	block_sz = 8192
	while True:
		buffer = u.read(block_sz)
		if not buffer:
		    break

		file_size_dl += len(buffer)
		f.write(buffer)
		status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
		status = status + chr(8)*(len(status)+1)
		print status,

	f.close()

    # urllib2.Request.urlretrieve(url, filename)
else:
    print("Harvard Inquirer lexical data found at {}".format(filename))

# Download nltk data
nltk.download("wordnet")
nltk.download("punkt")

print("\n3rd party data downloaded correctly.\n")
