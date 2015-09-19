import mechanize
from bs4 import BeautifulSoup
import re
import datetime
import argparse
import sys
import ConfigParser
import time


class CallerPy():

	def authenticate(self):
		url = 'http://www.truecaller.com/authenticate/'
		return url

	def twitter(self, user, pwd):
		
		param = 'twitter'
		url = self.authenticate()
		B.open(url+param)
		B.form = list(B.forms())[0]
		B['session[username_or_email]'] = user
		B['session[password]'] = pwd
		return B.submit()

	#def googlePlus():

	#def facebook():
	

	def truecaller(self, country, number):
		B.form = list(B.forms())
		B.follow_link(nr=1)
		q = B.open('http://www.truecaller.com/search/%s/%s' %(country, number))
		a = q.read()
		bs = BeautifulSoup(a)
		if '<hgroup id="result-profile-heading">' in a:
			for name in bs.find_all('hgroup',{"id":"result-profile-heading"}):
				nm = re.split(r'<.*?>', str(name))
				for i in nm:
					print i
			self.save(nm[2], country, number)


	def save(self, name, country, number):
		template = '''{
name::%s
number::%s
country::%s
}
''' %(name, number, country)
		log = open('log', 'a')
		log.write(template)
		log.close()
		

	def country_by_code(self, code):
		a = open('countries', 'r')
		b = a.read()
		p = re.findall('[a-z]{1,}', b)
		o = re.findall('[0-9]{1,}', b)
		for i, e in zip(p, o):
			if str(code) == str(e):
				return i

	def history(self):
		a = open('log', 'r').read()
		names = re.findall(r"name::(.*)", a)
		numbers = re.findall(r"number::(.*)", a)
		countries = re.findall(r"country::(.*)", a)
		
		for name, number, country in zip(names, numbers, countries):
			print name, '--', number, '--',  country

	def login_creds(self, param):
		config = ConfigParser.ConfigParser()
		config.read('callerpy.ini')
		user= config.get(param, 'username')
		pwd= config.get(param, "password")	
		return user, pwd
		
