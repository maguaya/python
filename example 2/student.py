class student:
	def __init__(self,first_name,last_name,age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
	def fullname(self):
		name = self.first_name+self.last_name
		return name

	def year_of_birth(self):
		return 2019-self.age
	def greeting(self):
			return "Hello {} you were born in {}".format(self.first_name,2019-self.age)

	def initials(self):
		text = self.first_name[0] +self.last_name[0]
		return text