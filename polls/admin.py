from django.contrib import admin
from polls.models import Question, Choice

#simple field order
#class QuestionAdmin(admin.ModelAdmin):
#    fields = ['pub_date', 'question_text']

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

#more complex, with fieldsets, and inline choices
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
