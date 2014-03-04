from django.contrib import admin
from polls.models import Choice, Poll #From tuto2: 
                          #https://docs.djangoproject.com/en/1.6/intro/tutorial02/

# Register your models here.
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
	#fields = ['pub_date', 'question']
	fieldsets=[
		(None,			{'fields': ['question']}),
		('Date information',	{'fields': ['pub_data'],'classes':['collapse']}),
	]
	inlines = [ChoiceInline]
	list_display = ['question','pub_data','was_published_recently','was_published_today']
	list_filter =['pub_data']
	search_fields=['question']

#admin.site.register(Poll)
admin.site.register(Poll,PollAdmin)
admin.site.register(Choice)
