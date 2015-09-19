class CallerPy():

	def authenticate(self):
		url = 'http://www.truecaller.com/authenticate/'
		return url

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

