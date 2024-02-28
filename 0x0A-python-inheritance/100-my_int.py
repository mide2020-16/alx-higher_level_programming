#!/usr/bin/python3

class MyInt(int):

	def __eq__(self, other):
		return super().__ne__(self, other)

	def __ne__(self, other):
		return super().__eq__(self, other)

MyInt.__setattr__(self, name, value)
