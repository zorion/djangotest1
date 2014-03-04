from django.db import models
import datetime #From tuto01
from django.utils import timezone #From tuto02
             # https://docs.djangoproject.com/en/1.6/intro/tutorial02/

# Create your models here.

class Poll(models.Model):
	question = models.CharField(max_length=200)
	pub_data = models.DateTimeField('date published:')
	def __str__(self):
		return self.question
	def was_published_today(self):
		return self.pub_data.date() == datetime.date.today()
	def was_published_recently(self):
		now = timezone.now()
		return now >= self.pub_data >= now - datetime.timedelta(days=2)
	was_published_recently.admin_order_field = 'pub_data'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published Recently?'

class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice = models.CharField(max_length=200)
	votes = models.IntegerField()
	def __str__(self):
		return self.choice


