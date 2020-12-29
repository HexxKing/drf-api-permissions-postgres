from django.test import TestCase
from django.contrib.auth.models import User
from .models import Publication

class BrainLogTests(TestCase):

  @classmethod
  def setUpTestData(cls):
    #create a user
    testuser1 = User.objects.create_user(
      username = 'testuser1', 
      password = 'abc123'
    )
    testuser1.save()

    #create a BrainLog publication
    test_publication = Publication.objects.create(
      author = testuser1,
      title = 'BrainLog Title',
      body = 'Body Content...'
    )
    testuser1.save()

  def test_brainlog_content(self):
    publication = Publication.objects.get(id=1)
    author = f'{publication.author}'
    title = f'{publication.title}'
    body = f'{publication.body}'
    self.assertEqual(author, 'testuser1')
    self.assertEqual(title, 'BrainLog Title')
    self.assertEqual(body, 'Body Content...')
