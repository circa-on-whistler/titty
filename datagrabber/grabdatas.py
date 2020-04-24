import os
import sys
from urllib.parse import urlparse

list_of_sites_filename = sys.argv[1]
list_of_sites = []
with open(list_of_sites_filename, "r") as f_list:
	list_of_sites = f_list.readlines()

visited_sites = []
for site in list_of_sites:
	if site.strip() == '': continue
	if urlparse(site).hostname in visited_sites: continue
	visited_sites.append(urlparse(site).hostname)
	os.system("python datagrabber.py " + site)
