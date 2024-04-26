from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Lesson, Badge, Quiz

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'
        widgets = {
              "content": CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="content"
              )
          }
        
class BadgeForm(forms.ModelForm):
    class Meta:
        model = Badge
        fields = '__all__'

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'


