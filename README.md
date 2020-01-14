The python script to extract domain names from a URL list, while ensuring the TLD being intact.

It'll strip any sub-domain or path from the URL and creates a new file with the unique domain list.

The script required the **TLDextract** library by John, for Python 3. More on the library and details at https://github.com/john-kurkowski/tldextract

Command to install: pip install tldextract

**Usage:**
- $chmod +x domain.py
- $./domain.py <filename>

**Note-1:** The input files must contain one URL in each line.
**Note-2:** The output is stored in the program folder itself as sorted_domain.txt.

Enjoy!!
