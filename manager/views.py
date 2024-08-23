from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Manager Index")

def add(request):
    return HttpResponse("Manager. Add article")

def edit(request, article_id):
    return HttpResponse(f"Manager. Edit id={article_id} article")

def delete(request, article_id):
    return HttpResponse(f"Manager. Delete id={article_id} article")