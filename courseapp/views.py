from django.shortcuts import render, redirect
from . forms import LessonForm, QuizForm, BadgeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *


# Create your views here.

@login_required
def add_lesson(request):
    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.author = request.user
            lesson.save()
            return redirect('home')
    else:
        form = LessonForm()
    return render(request, 'add_lesson.html', {'form': form})

@login_required
def add_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = QuizForm()
    return render(request, 'add_quiz.html', {'form': form})

@login_required
def add_badge(request):
    if request.method == 'POST':
        form = BadgeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BadgeForm()
    return render(request, 'add_badge.html', {'form': form})

@login_required
def view_lessons(request):
    lessons = Lesson.objects.all()
    return render(request, 'view_lessons.html', {'lessons': lessons})

@login_required
def view_quizzes(request):
    quizzes = Quiz.objects.all()
    return render(request, 'view_quizzes.html', {'quizzes': quizzes})

@login_required
def view_badges(request):
    badges = Badge.objects.all()
    return render(request, 'view_badges.html', {'badges': badges})

@login_required
def delete_lesson(request, id):
    lesson = Lesson.objects.get(id=id)
    lesson.delete()
    messages.info(request, 'Lesson deleted successfully')
    return redirect('view_lessons')

@login_required
def delete_quiz(request, id):
    quiz = Quiz.objects.get(id=id)
    quiz.delete()
    messages.info(request, 'Quiz deleted successfully')
    return redirect('view_quizzes')

@login_required
def delete_badge(request, id):
    badge = Badge.objects.get(id=id)
    badge.delete()
    messages.info(request, 'Badge deleted successfully')
    return redirect('view_badges')
# Compare this snippet from courseapp/urls.py:

# """
# URL configuration for courseapp app.
# """
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('add-lesson/', views.add_lesson, name='add_lesson'),
