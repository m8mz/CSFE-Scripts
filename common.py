import requests
import pickle
import os
import time
import hashlib
import re
from getpass import getpass
from bs4 import BeautifulSoup
HOME = os.environ['HOME']


class CSFE_User(object):
	"""This class will be your CSFE login and account that these GET requests will be performed through.
	This class will have a login, cookie, and request method to utilize the CSFE platform to gather information."""

	def __init__(self):
		self.username = "mhancock-gaillard"
		self.home = HOME
		self.cookiepath = HOME + '/temp/cookies/csfecookie'
		self.enc_pass = HOME + '/passwd/encrypted_pass.txt'
		self.cookie()

	def login(self):
		url = "https://enduranceoss.com/cs/oss_login.html"
		s = requests.session()
		username = self.username
		csfepass = getpass("Password: ")
		try:
			with open(self.enc_pass, 'r') as enc_pass:
				pass_ = enc_pass.readline()
				while hashlib.md5(csfepass.encode('UTF8')).hexdigest() != pass_.strip('\n'):
					print("Incorrect Password.")
					csfepass = getpass("Password: ")
			creds = {
				"oss_user_name": username,
				"oss_password": csfepass,
				"oss_login": "Login"
			}
			r = s.post(url, data=creds)
			if r.status_code == 200:
				with open(self.cookiepath, 'wb') as f:
					pickle.dump(s.cookies, f)
					print("Successfully logged in!")
			else:
				print("Failed log in!")
		except FileNotFoundError:
			print("Encrypted Pass File Not Found.")

	def cookie(self):
		if os.path.isfile(self.cookiepath):
			filetime = os.path.getmtime(self.cookiepath)
			timenow = time.time()
			diff = timenow - filetime
			if diff > 28000:
				print("Cookie has expired! Provide password.")
				self.login()
		else:
			print("No cookie found! Provide password.")
			self.login()

	def send_request(self, link, dataObject):
		cookies = pickle.load(open(self.cookiepath, "rb"))
		res = requests.post(link, data=dataObject, cookies=cookies)
		if link == "https://admin.enduranceoss.com/csfe/widgets/vps_info_new.cmp":
			return res.content
		else:
			htmltext = BeautifulSoup(res.content, 'lxml')
			return htmltext

	def post_request(self, link, dataObject):
		try:
			cookies = pickle.load(open(self.cookiepath, "rb"))
		except:
			print("Couldn't load cookies for the request")
		else:
			res = requests.posts(self.link, data=self.dataObject, cookies=cookies)
			return res.status_code

	def isloggedin(self):
		try:
			cookie = pickle.load(open(self.cookiepath, "rb"))
		except:
			print("Cookie file could not be opened")

		username = re.findall(r'UserName%3D([\w-]+)', str(cookie))[0]
		if username == self.username:
			return True
		else:
			print("Not logged in.. please login first.")
			self.login()

	def get_user(self, arg):
		# Domain Arg
		if re.match(r'[a-z0-9]{4,}\.[a-z]+', arg):
			link = 'https://admin.enduranceoss.com/csfe/search.html'
			dataObject = {
				"search_type": "domain",
				"advanced_search": arg
			}
			result = self.send_request(link, dataObject)
			for table in result.find_all('table'):
				for td in table.find_all('td'):
					for a in td.find_all('a'):
						return a.text
		# IP Arg
		elif re.match(r'[0-9\.]+', arg):
			link = 'https://admin.enduranceoss.com/csfe/search.html'
			dataObject = {
				"search_type": "VPSIP",
				"advanced_search": arg
			}
			req = self.send_request(link, dataObject)
			acct = req.find_all('a')[-1]
			if acct.text != 'Log Out':
				return acct.text
			else:
				return "Not found!"
		else:
			# Going to assume it was the username provided
			return arg
