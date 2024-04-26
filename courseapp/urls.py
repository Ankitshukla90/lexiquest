from django.urls import path
from . import views

urlpatterns = [
    path('view_lessons', views.view_lessons, name='view_lessons'),
    path('view_quizzes', views.view_quizzes, name='view_quizzes'),
    path('view_badges', views.view_badges, name='view_badges'),
    path('add_lesson', views.add_lesson, name='add_lesson'),
    path('add_quiz', views.add_quiz, name='add_quiz'),
    path('add_badge', views.add_badge, name='add_badge'),
    path('delete_lesson/<int:id>', views.delete_lesson, name='delete_lesson'),
    path('delete_quiz/<int:id>', views.delete_quiz, name='delete_quiz'),
    path('delete_badge/<int:id>', views.delete_badge, name='delete_badge'),
]

api_urlpattern = [
    
]
# # ]
#
# Compare this snippet from courseapp/views.py: