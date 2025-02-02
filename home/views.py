from django.shortcuts import render
from django.templatetags.static import static

def home(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def skills(request):
    return render(request, 'skills.html', {})

def project(request):
    projects = [
        {
            "title": "ToDo List",
            "description": "This project is a Python ToDo List app for managing tasks with features like add, remove, view, save, load, and append.",
            "github_url": "https://github.com/shivamr021/ToDo-List",
            "image": static("projects/todo_list.png"),
        },
        {
            "title": "Rock Paper Scissors",
            "description": "A Python implementation of Rock-Paper-Scissors, allowing users to play against the computer with input validation and multiple rounds.",
            "github_url": "https://github.com/shivamr021/rock-paper-scissors",
            "image": static("projects/rock_paper_scissors_game.png"),
        },
    ]
    return render(request, 'project.html', {'projects': projects})

def certifications(request):
    return render(request, 'certifications.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def experience(request):
    return render(request, 'experience.html', {})

def assignments(request):
    return render(request, 'assignments.html')