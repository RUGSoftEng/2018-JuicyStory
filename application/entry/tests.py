from django.test import TestCase
from django.contrib.auth.models import User

class EntryTests(TestCase):

	def setUp(self):
		''' Set up a random user to rand tests '''
		User.objects.create_user('testname', 'test@mail.com', 'testpassword')

	def test_login(self):
		''' test if the user can be successfully authenticated for a login '''
		user = User.objects.get(username='testname')
		self.assertTrue(user.is_authenticated, False)
		self.client.login(username=user.username, password=user.password)
		self.assertTrue(user.is_authenticated, True)

	def test_signup(self):
		''' TODO :: Testing the signup of the applicaiton '''
		self.assertTrue(True)

	def test_logout(self):
		''' test if the user can be successfully logged out of an account '''
		user = User.objects.get(username='testname')
		self.assertTrue(user.is_authenticated, True)
		self.client.logout()
		self.assertTrue(user.is_authenticated, False)

	def test_form_validity(self):
		''' TODO :: Testing the form validity of the signup, login '''
		self.assertTrue(True)