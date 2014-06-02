__author__ = "Tony Ling"
# Change Log:
#    5/29/14 - File created.
#              CKANApi created for generic CKAN api search.
#              datastore search method added to CKAN class.
#    5/30/14 - CKANApiASP class created specifically to filter out
#              libraries from results for specific datastore.
#              Added support for queries and limit
#
#  Resource_id keys: 
#    1e042827-d69d-48f0-a2ba-1df13c3c307e: After-school programs
#    d749fc15-4c9c-4ed9-b07f-9f2481dd1f1a: NYC DOE 21st Century Learning Centers
#
#  Resources:
#    http://stackoverflow.com/questions/19697846/python-csv-to-json

import requests
import json
import csv
import sys

class CKANApi:
	"""

	Generic CKANApi class used for retrieving data
	
	Constructor parameters:
	  site      = base website ex: 'http://nycdoe.pediacities.com'
	  api_level = api level if applicable, default is None
	"""
	def __init__(self, site, api_level=None):
		if (api_level):
			self.api = "{0}/api/{1}/action/".format(site, api_level)
		else:
			self.api = "{0}/api/action/".format(site)
		print("Data api: ", self.api)

	def datastore_search(self, resource_id, q=None, limit=None):
		"""

		Retrieves resouces using HTTP get API

		Parameters:
		  resource_id = resource id of data
		  q           = query
		  limit       = number of elements returned
		
		Returs JSON object if successful API call, None otherwise
		"""

		url = '{0}datastore_search?resource_id={1}'.format(self.api, resource_id)
		if (q is not None):
			url += '&q={0}'.format(q)
		if (limit is not None):
			url += '&limit=%d' % (limit)
		try:
			response = requests.get(url, timeout=5.0)
		except requests.exceptions.Timeout:
			sys.stderr.write("  Exception: connection timed out")
			return None

		json_obj = json.loads(response.text)
		# json object success field True if resources are found
		if (json_obj and json_obj["success"] == True):
			with open("{0}.json".format(resource_id), "w") as f:
				for ele in json_obj['result']['records']:
					f.write(json.dumps(ele, 
						sort_keys=True, indent=4, separators=(',', ': ')))
		return json_obj

class CKANApiASP(CKANApi):
	"""

	Specialized class specificially for filtering libraries
	from After School Programs at 'http://nycdoe.pediacities.com'

	Subclass of CKANApi with custom method datastore_search_afterschool
	"""
	def __init__(self):
		CKANApi.__init__(self, 'http://nycdoe.pediacities.com')
	
	def datastore_search_afterschool(self, resource_id, q=None, limit=None):
		"""

		Retrieves 'After-school programs' resources

		Parameters:
		  resource_id = "1e042827-d69d-48f0-a2ba-1df13c3c307e"
		  q           = query
		  limit       = number of elements returned

		Returns JSON object if successfull API call, None otherwise
		"""
		resource_id = "1e042827-d69d-48f0-a2ba-1df13c3c307e"
		url = '{0}datastore_search?resource_id={1}'.format(self.api, resource_id)
		if (q is not None):
			url += '&q={0}'.format(q)
		if (limit is not None):
			url += '&limit=%d' % (limit)
		try:
			response = requests.get(url, timeout=5.0)
		except requests.exceptions.Timeout:
			sys.stderr.write("  Exception: connection timed out")
			return None

		json_obj = json.loads(response.text) 
		# json object success field True if resources are found
		if (json_obj and json_obj["success"] == True):
			with open("{0}.json".format(resource_id), "w") as f:
				for ele in json_obj['result']['records']:
					if (ele['SETTING'] != 'Library'):  # filters out libraries
						f.write(json.dumps(ele, 
							sort_keys=True, indent=4, separators=(',', ': ')))
		return json_obj

if __name__ == "__main__":
	ckan = CKANApi('http://nycdoe.pediacities.com')
	ckanASP = CKANApiASP()
#	str = ckanASP.datastore_search_afterschool()
#	str = ckan.datastore_search("d749fc15-4c9c-4ed9-b07f-9f2481dd1f1a")
#	str = ckan.datastore_search("1e042827-d69d-48f0-a2ba-1df13c3c307e", "Library", 10)