from django.contrib import admin
from .models import Question, Poll, Choice


class ChoiceAdmin(admin.ModelAdmin):
	search_fields = ('choice_text', )
	list_display = ('choice_text', 'question')
	class Meta:
		model = Choice

		
class InlineChoiceAdmin(admin.TabularInline):
	model = Choice
	

class QuestionAdmin(admin.ModelAdmin):
	inlines = [InlineChoiceAdmin, ]
	list_display = ('question_text', 'polls')
	
	def polls(self, obj):
		return ', '.join(obj.poll_set.all().values_list('name', flat=True))
	
	class Meta:
		model = Question
		
		
class PollAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug')
	
	class Meta:
		model = Poll
		
		
admin.site.register(Question, QuestionAdmin)
admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
