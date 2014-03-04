from django.shortcuts import render,get_object_or_404 #error 404 from tuto03
from django.http import HttpResponse,Http404,HttpResponseRedirect #from tuto03 and 04
                       # https://docs.djangoproject.com/en/1.6/intro/tutorial03/
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse 
from django.views import generic
from django.utils import timezone #tuto05

from polls.models import Poll,Choice

# Create your views here.

#OLD index from tuto03
def index(request):
	latest_5_poll_list = Poll.objects.order_by('-pub_data')[:5]
	template = loader.get_template('polls/index.html') #See below how to use templates
	context = RequestContext(request, {
		'latest_poll_list': latest_5_poll_list,
	})
	return HttpResponse(template.render(context))


#OLD detail from tuto03
def detail(request,poll_id):
	try:
		poll = Poll.objects.get(pk=poll_id)
	except Poll.DoesNotExist:
		raise Http404
	#Here we use the shortcut to render with the template
	#No need context here, it is just the poll
	return render(request,'polls/detail.html',{'poll':poll})


#OLD results from tuto03
def results(request,poll_id):
	poll = get_object_or_404(Poll, pk=poll_id)
	return render(request,'polls/results.html',{'poll':poll})

#OK, from tuto03
def vote(request,poll_id):
	p = get_object_or_404(Poll,pk=poll_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice_s'])
	except (KeyError, Choice.DoesNotExist):
		#Redisplay the poll voting form.
		return render(request, 'polls/detail.html', {
			'poll': p,
			'error_message':"You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		#Prevents doubleposting if user hits the back button
		return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))



###################Tuto04
class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_poll_list'
	
	def get_queryset(self):
		"""Return the last five published polls."""
		#return Poll.objects.order_by('-pub_data')[:5] #tuto04
		return Poll.objects.filter( #tuto05
			pub_data__lte=timezone.now() #not in future
		).order_by('-pub_data')[:5] 

class DetailView(generic.DetailView):
	template_name= "polls/detail.html"
	model = Poll
	def get_queryset(self):
		"""
		Excludes polls that aren't published yet.
		"""
		return Poll.objects.filter(pub_data__lte=timezone.now())

class ResultsView(generic.DetailView):
	model = Poll
	template_name='polls/results.html'
	def get_queryset(self):
		"""
		Excludes polls that aren't published yet.
		"""
		return Poll.objects.filter(pub_data__lte=timezone.now())


