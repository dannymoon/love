from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'survey/index.html')
def answer1(request):
    return redirect('/page1')
def answer2(request):
    return redirect('/page2')
def page2(request):
    return render(request, 'survey/page2.html')
def page1(request):
    return render(request, 'survey/page1.html')