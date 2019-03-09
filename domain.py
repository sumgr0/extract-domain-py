#!/usr/bin/env python3

import os
import sys
import tldextract

#Files in use
subdom = str(input('Enter file path: ')) #file input for URL list
raw = "raw_domain.txt" # raw file for working
sort = "sorted_domain.txt" # unique value of domain listing

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
