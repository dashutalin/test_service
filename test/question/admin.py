from django.contrib import admin
from .models import Answer, Group, Set, Question


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'group',
    )
    search_fields = ('question', 'group') 
    list_filter = ('group',)


class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'ans',
        'is_right',
        'question',
    )
    search_fields = ('question', 'ans') 
    list_filter = ('question',)


admin.site.register(Answer, AnswerAdmin)
admin.site.register(Group)
admin.site.register(Set)
admin.site.register(Question, QuestionAdmin)
