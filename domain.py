#!/usr/bin/env python3

import os
import sys
import tldextract

#Check command line for inputs
if len(sys.argv) < 3:
	print("Wrong parameter")
	print("python3 domain.py input_file output_file")
	sys.exit(1)

#Reading command line arguments
subdom = (sys.argv[1])
sort = (sys.argv[2])
raw = "raw_domain.txt"

with open(subdom) as o:
	if os.path.exists("raw_domain.txt"):

		print(">>Removing existing Raw Domain file!")
		os.remove(raw)

		print(">>Creating new Raw Domain file!")
		
		with open (raw,"w") as r:
			for url in o:
				ext = tldextract.extract(url)
				domain = ext.registered_domain
				r.write(domain)
				r.write('\n')
	else:
		with open (raw,"w") as r:
			for url in o:
				ext = tldextract.extract(url)
				domain = ext.registered_domain
				r.write(domain)
				r.write('\n')
				
with open(raw,"r") as rr:
	rr = [item.lower().replace("\n", "") for item in rr.readlines()]
with open(sort, "w") as s:
	for item in sorted(set(rr)):
		s.write(item.lower()+"\n")

print(">>Removing Raw Domains file")
os.remove(raw)

print ("Task completed!")