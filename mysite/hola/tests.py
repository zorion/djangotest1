from django.test import TestCase
from hola.models import Greeting

# Create your tests here.
class SimpleTest(TestCase):
	def setupGreeting(self,ctnt):
		Greeting(content=ctnt).save()

	def test_setup(self):
		content="This is a test"
		self.setupGreeting(content)
		self.assertEqual(1, len(Greeting.objects.all()))
		self.assertEqual(content, Greeting.objects.all()[0].content)

