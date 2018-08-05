# i=0
# a=0

# counter=0
# while i<10000:
# 	i+=counter
# 	counter+=1
# print(counter)

# while i<10000 and i%2==0:
# 	i+=counter
# 	counter+=1
# print(counter)


def is_prime(x):

	for i in range (2,x):
		if x%i==0:
		  return ("not prime")

	return("prime")
	


class superhero:

	def __init__(self,name,superpower,strength):
		self.name=name
		self.superpower=superpower
		self.strength=strength

	 def print_name(self):
	      print("My name is", self.name)
	      
	 def save_civilian(self,work):
	 	 self.strength=self.strength-work		







	

