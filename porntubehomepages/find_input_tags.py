from bs4 import BeautifulSoup
import os

def find_parent_form(tag):
	if tag.parent != None and tag != None:
		if tag.name != 'body':
			if tag.parent.name == 'form':
				return tag.parent
			else:
				return find_parent_form(tag.parent)
		else:
			return None
	else:
		return None
	return None

def parse_and_print(html_src):
	html = BeautifulSoup(html_src, features="html.parser")
	for input_tag in html.find_all("input", attrs={"type", "text"}):
		parent_form = find_parent_form(input_tag)
		#print(parent_form)
		if parent_form != None:
			print ("\ttag: " + str(input_tag) + " / form: " + str(parent_form))
		else:
			print ("\ttag: " + str(input_tag))

for dirpath, dnames, fnames in os.walk("./"):
	for file in fnames:
		if file.endswith(".html"):
			print(file)
			with open(file, "r") as homepage:
				parse_and_print(homepage.read())
