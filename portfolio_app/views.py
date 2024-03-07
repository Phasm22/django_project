from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
    # Render index.html
    student_active_portfolios = Student.objects.select_related('portfolio').filter(portfolio__is_active=True)
    print("active portfolio query set", student_active_portfolios)
    return render(request, 'portfolio_app/index.html', {'student_active_portfolios': student_active_portfolios})