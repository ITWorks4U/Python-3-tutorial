#!/usr/bin/python3

"""
	Unit testing allows you to test
	specific scenarios for your project.

	In math.py we're using simple
	arithmetic operations, thus
	we can assume an expected result
	and also specific errors, like
	division by zero.

	The result of test cases may be:
	.	:=	executed successfully
	x	:=	expected a failure
	u	:=	unexpected successes
	s	:=	skipped that test
	F	:=	failed test

	hint: every test must start with test as
	prefix, otherwise this test will never
	execute
"""

#	gain access to unit testing
import unittest as ut

#	using everything from our math module
import mathTest as m

#	-------------
#	Test cases for math operations.
#	-------------
class TestingMath(ut.TestCase):
	#	-------------
	#	in use to create required
	#	objects, variables, ...
	#	before a test begins
	#	-------------
	def setUp(self):
		self.bm = m.BasicMath()
	#end init

	#	-------------
	#	clean up between each
	#	test to make sure, that
	#	no orphan object exists
	#	-------------
	def tearDown(self):
		del self.bm
	#end disposing

	#	-------------
	#	testing, if 3 + 4 = 7
	#	-------------
	def testAdd(self):

		#	-------------
		#	assert := we're assuming, that a certain
		#	condition shall be true
		#	-------------
		#	if true, no error appears here,
		#	if false, an AssertionError appears, which
		#	marks this method as failed
		#	-------------
		#	Since an AssertionError may appear, we're not
		#	forced to handle this exception. It will be
		#	handled automatically.
		#	-------------
		self.assertEqual(self.bm.addition(3,4), 7, '3 + 4 = 7!')
	#end method

	#	-------------
	#	Division by zero fails and this test will also
	#	fail, however, we can handle this failure,
	#	when we're expected that.
	#	-------------
	#	use @[module].expectedFailure to handle that
	#	-------------
	@ut.expectedFailure
	def testDivideByZero(self):
		self.assertEqual(self.bm.divide(15,0), 0, 'Wait a minute...!')
	#end method

	#	-------------
	#	Testing, that this raises our math exception class,
	#	when we're using arguments, which are not decimal (int).
	#	-------------
	def testWrongArguments(self):
		bm = m.BasicMath()

		with self.assertRaises(m.MathException):
			bm.addition('howdy', 'ho')
		#end with
	#end method

	#	-------------
	#	Skipping this test for a later purpose.
	#	-------------
	def testSkipTest1(self):
		with self.skipTest("skipped at the moment"):
			bm.addition('3', 9)
		#end with
	#end method

	#	-------------
	#	Also possible to skip a test.
	#	-------------
	@ut.skip("demonstrating skipping")
	def testSkipTest2(self):
		self.fail("epic fail")
	#end method
#end class

#	-------------
#	Test cases for file operations.
#	-------------
from fileTesting import readFromFile

"""
	Using file operations instead and
	try to figure out, if these test(s)
	is/are successful or failed.
"""
class TestingFileOperations(ut.TestCase):
	def setUp(self) -> None:
		self.fileName = "test.txt"
	#end set up

	def tearDown(self) -> None:
		del self.fileName
	#end tear down

	def testReadFileFails(self):
		with self.assertRaises(FileNotFoundError):
			readFromFile(self.fileName)
		#end with
	#end method
#end class

if __name__ == '__main__':
	#	launching the unit tests
	ut.main()
#end if