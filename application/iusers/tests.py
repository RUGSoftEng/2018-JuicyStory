from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class IuserTests(TestCase):
		
	def test_view(self):
		''' Testing if the url matches and the response code '''
		response = self.client.get(reverse('iusers:list_iusers'))
		self.assertEquals(response.status_code, 302)
		# '/?next=/' makes sure that you have been authneticated as a user 
		self.assertEquals(response.url, '/entry/login/?next=/iusers/listIusers/')