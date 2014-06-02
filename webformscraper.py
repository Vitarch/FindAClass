__author__ = "Tony Ling"
# Change Log:
#    5/29/14 - File creation.  Added TonyHTMLParser Class, and
#              WebFormParserNYCChildCare class.
#              get_web_form_results method added to obtain data.
#              HTML Parser class used to parse through obtained data.
#    5/30/14 - Restructured comments, renamed WebFormParser to
#              WebFormParserNYCChildC since it was not a generic class
#
# Resources:
#  http://www.blog.pythonlibrary.org/2012/06/08/python-101-how-to-submit-a-web-form/
#  http://docs.python-requests.org/en/latest/

from html.parser import HTMLParser
import requests
import webbrowser
import json

# HTMLParser used within WebFormParserNYCChildCare
class TonyHTMLParser(HTMLParser):
	"""

	HTML parser meant for use in WebFormParser class
	
	Constructor parameters:
	  url = website url
	  print_count = True to print to stdout number of child services found
	"""
	def __init__(self, url, print_count = False):
		HTMLParser.__init__(self)
		self.cur_tag = "nil"
		self.url = url
		self.print_count = print_count
	def handle_starttag(self, tag, attrs):
		self.cur_tag = tag
		# if (tag == "br"):
		# 	print("Start tag:", tag)
		# 	for attr in attrs:
		# 		print("		attr:", attr)
	def handle_data(self, data):
		if (self.print_count and self.cur_tag == "br" and data.strip()):
			print("{0} child care services found".
			      format(data.strip().split()[0]))

class WebFormParserNYCChildCare:
	"""

	Automated web form info harvest for website HTML form
	https://a816-healthpsi.nyc.gov/ChildCare/SearchAction2.do'

 	Constructor parameters:
      url = website url
	"""
	def __init__(self):
		self.url = 'https://a816-healthpsi.nyc.gov/ChildCare/SearchAction2.do'
	def get_web_form_results(self, name, program_type, borough, 
						 neighborhood, zip, permit_no):
		""" 

		Obtains web form results from website using the passed in arguments
		Set parameters to None if no value

		Parameters:
			name         = facilty name
			program_type = 'INFANT TODDLER' or 'PRESCHOOL'
			borough      = one of the five borough
			zip          = zip code
			neighborhood = one of the neighborhood in NYC
			permit_no    = permit number
		No return value
		"""

		# Use a Session object to keep alive connection to server
		# required to query page offset
		s = requests.Session()

		# Search results requires 'getNewResults' set to 'true'
		payload = {'getNewResult':'true'}	
		# Inserting arguments into proper data 
		if name is not None:
			payload['facilityName'] = name
		if program_type is not None:
			payload['ageRange'] = program_type
		if borough is not None:
			payload['borough'] = borough
		if neighborhood is not None:
			payload['neighborhood'] = neighborhood
		if zip is not None:
			payload['zip'] = zip
		if permit_no is not None:	
			payload['permit_no'] = permit_no

		try:
			response = s.post(self.url, data=payload, timeout=5.0)
		except requests.exceptions.Timeout:
			sys.stderr.write("  Exception: connection timed out")

		# WIP Code for going to next pages
		# offset = 10
		# url2 = self.url + '?pager.offset={0}'.format(offset)
		# response2 = s.get(url2)
		# #print(response2.text)

		parser = TonyHTMLParser(self.url, True)
		parser.feed(response.text)
		# parser.feed(open("test.html").read())
		# with open("test.html", "w") as f:
		# 	f.write(response.text)

		# webbrowser.open("test.html")

		# with open("test2.html", "w") as f:
		# 	f.write(response2.text)

		# webbrowser.open("test2.html")

if __name__ == "__main__":
	web_parser = WebFormParserNYCChildCare()
	web_parser.get_web_form_results(None, None, None, None, None, None)
