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

class StudentListView(generic.ListView):
    model = Student
class StudentDetailView(generic.DetailView):
    model = Student
class PortfolioListView(generic.ListView):
    model = Portfolio
class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    
    def get_context_data(self, **kwargs):
        projects = Project.objects.all()
        student_portfolio_projects = []
        for project in projects:
            if project.portfolio.title == self.object.title:
                student_portfolio_projects.append(project)
        context = super(PortfolioDetailView, self).get_context_data( **kwargs)
        context["student_portfolio_projects"] = student_portfolio_projects
        return context

    def __str__(self):
        return self.id
class ProjectListView(generic.ListView):
    model = Project
class ProjectDetailView(generic.DetailView):
    model = Project
