__author__ = "Tony Ling"
# Change Log:
#    5/29/14 - File created.
#              CVSHandler class used to handle cvs files.
#              Class downloads cvs files and converts into JSON text file.
#    5/30/14 - Changed download_cvs_file method to down_load_cvs_file_to_JSON
#              Replaced download_cvs_file with generic method to download a
#              CVS file from any url and save in directory
#

import requests
import json
import csv
import sys
import os

class CVSHandler():
	def __init__(self, timeout=5.0):
		self.timeout = timeout
	def download_cvs_file(self, url, directory=""):
		"""

		Downloads a cvs file and saves it in a directory
		
		Parameters:
		  url = location of cvs file
		  directory = directory where to save file, ex: "test/"
		
		No return value
		"""
		try:
			r = requests.get(url, timeout=self.timeout)
		except requests.exceptions.Timeout:
			sys.stderr.write("  Exception: connection timed out")
			return None
		file_name = "{0}{1}".format(directory, url.rsplit('/', 1)[1])
		try:
			with open(file_name, 'w') as f:
				f.write(r.text)
		except Exception as e:
			print(e, file=sys.stderr)

	def download_cvs_file_to_JSON(self, url, directory=""):
		"""

		Downloads a cvs file, converts it to JSON and saves it in a directory
		
		Parameters:
		  url = location of cvs file
		  directory = directory where to save file, ex: "test/"
		
		No return value
		"""
		try:
			r = requests.get(url, timeout=self.timeout)
		except requests.exceptions.Timeout:
			sys.stderr.write("  Exception: connection timed out")
			return None
		file_name = "{0}".format(url.rsplit('/', 1)[1])
		dict_reader = csv.DictReader(r.text.splitlines())
		try:
			with open("{0}{1}.json".format(
				directory, file_name.rsplit('.',1)[0]), 'w') as f:
				for ele in dict_reader:
					f.write(json.dumps(ele, 
									sort_keys=True, indent=4, separators=(',', ': ')))
		except Exception as e:
			print(e, file=sys.stderr)

if __name__ == "__main__":
	test = CVSHandler()
	test.download_cvs_file_to_JSON("https://nyc-doe.s3.amazonaws.com/2014-05-07T20:06:17.342Z/nyc-summer-quest-sample-data-set.csv") 