from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice


# Register your models here.
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 5


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 5


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question)
admin.site.register(Choice)
