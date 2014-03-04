#from django.shortcuts import render
from django.views import generic
#from django.views.generic import direct_to_template
from django.core.cache import cache
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse 
from hola.models import Greeting

MEMCACHE_GREETINGS = 'greetings'

# Create your views here.
class IndexView(generic.ListView):
	template_name='hola/index.html'
	context_object_name='greetings'
	def get_queryset(self):
		greetings = cache.get(MEMCACHE_GREETINGS)
		if greetings is None:
			greetings = Greeting.objects.all().order_by('-date')[:10]
			cache.add(MEMCACHE_GREETINGS,greetings)
		return greetings
	

def sign(request):
	ct=request.POST['content']
	g = Greeting(content=ct,date=timezone.now())
	if request.user.is_authenticated():
		g.author = request.user
	g.save()
	#cache.clear(MEMCACHE_GREETINGS)
	return HttpResponseRedirect(reverse('hola:index'))


