from django.test import TestCase
from .models import InstagramUser
from django.contrib.auth.models import User

class DatabaseTests(TestCase):

	#Set up 1000 random users and test them.
	def setUp(self):
		size = 1000
		george = User.objects.create_user('testname', 'test@mail.com', 'testpassword')
		for i in range(0, size):
			username = "Test" + str(i)
			#print(username)
			InstagramUser.objects.create(username=username, owner=george)

	#The actual test of asserting that the names match
	def test_users(self):
		size = 1000
		for i in range(0, size):
			username = "Test" + str(i)
			iuser = InstagramUser.objects.get(username=username)
			self.assertEqual(iuser.username, username)
