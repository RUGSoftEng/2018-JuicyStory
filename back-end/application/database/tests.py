from django.contrib.auth.models import User
from django.utils import timezone
from django.test import TestCase
from .models import (InstagramUser, ScheduledImage)


class DatabaseTests(TestCase):
  """ Tests for the database module """

  def setUp(self):
    ''' Set up 1000 random users and test them '''
    size = 1000
    george = User.objects.create_user('testname', 'test@mail.com', 'testpassword')
    for i in range(1, size):
      username = "Test" + str(i)
      iuser = InstagramUser.objects.create(username=username, owner=george)
      ScheduledImage.objects.create(username=iuser.username, upload_date=timezone.now(), is_story=False)

  def test_iusers_scheduledImage(self):
    ''' The actual test of asserting that the names match '''
    size = 1000
    for i in range(1, size):
      username = "Test" + str(i)
      iuser = InstagramUser.objects.get(username=username)
      image = ScheduledImage.objects.get(username=iuser.username)
      self.assertEqual(iuser.username, username)
      self.assertEqual(image.username, username)

  def test_more(self):
    self.assertEqual(1 + 1, 2)
