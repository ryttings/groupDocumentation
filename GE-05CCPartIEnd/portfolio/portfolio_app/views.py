from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic # pulled from internet source in 20231014LogCmd.txt
from .models import Student
from .models import Portfolio
from .models import Project

# Create your views here.
def index(request):
# Select student objects, related to portfolio, where active = True
    student_active_portfolios = Student.objects.select_related('portfolio').all().filter(portfolio__is_active=True)
    print("active portfolio query set", student_active_portfolios)
    return render( request, 'portfolio_app/index.html',
    {'student_active_portfolios':student_active_portfolios})

    portfolio_student_owner = Portfolio.objects.select_related('student').all()
    print("active portfolio query set", portfolio_student_owner)
    return render( request, 'portfolio_app/index.html',
    {'portfolio_student_owner':portfolio_student_owner})

    student_portfolio_projects = Project.objects.all().filter(title__icontains=)
    print("portfolio projects query set", student_portfolio_projects)
    return render( request, 'portfolio_app/index.html',
    {'student_portfolio_projects':student_portfolio_projects})
class StudentListView(generic.ListView):
    model = Student
class StudentDetailView(generic.DetailView):
    model = Student
class PortfolioListView(generic.ListView):
    model = Portfolio
class PortfolioDetailView(generic.DetailView, request):
    model = Portfolio
class ProjectListView(generic.ListView):
    model = Project
class ProjectDetailView(generic.DetailView):
    model = Project
