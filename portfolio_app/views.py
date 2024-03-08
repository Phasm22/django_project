from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import *
from .forms import ProjectForm, PortfolioForm, CreateUserForm, StudentForm

# Create your views here.
def index(request):
    # Render index.html
    student_active_portfolios = Student.objects.select_related('portfolio').filter(portfolio__is_active=True)
    print("active portfolio query set", student_active_portfolios)
    return render(request, 'portfolio_app/index.html', {'student_active_portfolios': student_active_portfolios})

class PortfolioDetailView(DetailView):  # new line
    model = Portfolio  # new line
    template_name = 'portfolio_app/portfolio_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Projects'] = Project.objects.filter(portfolio=self.object)
        return context

class StudentListView(generic.ListView):
    model = Student

class StudentDetailView(generic.DetailView):
    model = Student

def createProject(request, portfolio_id):
    form = ProjectForm()
    portfolio = Portfolio.objects.get(pk=portfolio_id)

    if request.method == 'POST':
        # Create a new directory with form data and portfolio_id
        project_data = request.POST.copy()
        project_data['portfolio_id'] = portfolio_id
        form = ProjectForm(project_data)
        if form.is_valid():
            # Save the form without committing to the database
            project = form.save(commit=False)
            # Set  the portfolio relationship
            project.portfolio = portfolio
            project.save()
            
            # Redirect back to the portfolio detail page
            return redirect('portfolio-detail', portfolio_id)
    context = {'form': form}
    return render(request, 'portfolio_app/project_form.html', context)