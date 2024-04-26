from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('lesson', views.lesson, name='lesson'),
    path('badge', views.badge, name='badge'),
    path('certificate', views.certificate, name='certificate'),
    path('quizes', views.quizes, name='quizes'),
    path('lessonquiz', views.lessonquiz, name='lessonquiz'),
]

api_urlpattern = [
    
]
# # ]
#
# Compare this snippet from courseapp/views.py: