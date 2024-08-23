from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("<h1>Articles Index</h1>")


def special_case_2023(request):
    return HttpResponse("<h1>Special Case 2023</h1>")


def year_archive(request, year):
    return HttpResponse(f'<h1>Year {year} Archive</h1>')


def month_archive(request, year, month):
    return HttpResponse(f"<h1>{year}-{month}<br>Archive</h1>")
