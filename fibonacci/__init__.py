from check50 import *

class fibonacci(Checks):

	@check()
	def exists(self):
		"""fibonacci.c exists"""
		self.require("fibonacci.c")

	@check("exists")
	def compiles(self):
		"""fibonacci.c compiles"""
		self.spawn("clang -o fibonacci fibonacci.c -lcs50 -lm").exit(0)
