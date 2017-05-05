import urllib2 #Extensible library for opening URLs
import os #Miscellaneous operating system interfaces for file operations

links = open('MSFTFreeEbooks.txt') #Opening the file which contains all the links
for link in links:
	try:
		data = urllib2.urlopen(link)
		#print data

		parseobj = urllib2.urlparse.urlparse(data.url) #Parsing the URL for retrieving the filename
		#print parseobj 

		filename = os.path.basename(parseobj.path) #basename extracts the end file name
		#print "Downloaded "+filename 

		if os.path.isfile(filename):
			print filename + " already exists"
		else:			
			
				print "Downloading " + filename
				urldata = data.read() #Read the contents of the file
				f = open(filename,'wb') #Give the file, the extracted name, wb for binary write
				f.write(urldata)
				f.close #Close the file after writing			
				print "Downloaded "+filename

	except Exception: #If the URL is broken
		None			