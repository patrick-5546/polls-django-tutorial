from django.contrib import admin

from .models import Choice, Question

# tabular makes fields in columns instead of one after the other for stacked (saves room)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # minimum number of choices created per question

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]  # choices are edited on question page
    # fields to display in page that displays all questions
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']  # add filter for pub_date
    search_fields = ['question_text']  # search textbox by question_text

# If you want to add to admin home page
admin.site.register(Question, QuestionAdmin)