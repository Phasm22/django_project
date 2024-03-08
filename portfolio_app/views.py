from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
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
        context['action'] = 'Update'
        context['object_type'] = 'Project'
        context['Projects'] = Project.objects.filter(portfolio=self.object)
        return context

class PortfolioUpdateView(UpdateView):
    model = Portfolio
    form_class = PortfolioForm
    template_name = 'portfolio_app/project_form.html'  # replace with your actual template
    context_object_name = 'portfolio'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Update'
        context['object_type'] = 'Portfolio'
        return context
    

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'portfolio_app/project_form.html'  # replace with your actual template
    context_object_name = 'project'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Update'
        context['object_type'] = 'Project'
        return context
    
    def get_success_url(self):
        return reverse('portfolio-detail', kwargs={'pk': self.object.portfolio.id})
    
class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'portfolio_app/project_confirm_delete.html'  # replace with your actual template
    success_url = reverse_lazy('projects')

    def get_success_url(self):
        portfolio_id = self.object.portfolio.id
        return reverse('portfolio-detail', args=[portfolio_id])
class StudentListView(generic.ListView):
    model = Student

class StudentDetailView(generic.DetailView):
    model = Student

def createProject(request, pk):
    form = ProjectForm()
    portfolio = Portfolio.objects.get(pk=pk)

    if request.method == 'POST':
        # Create a new directory with form data and portfolio_id
        project_data = request.POST.copy()
        project_data['portfolio_id'] = pk
        form = ProjectForm(project_data)
        if form.is_valid():
            # Save the form without committing to the database
            project = form.save(commit=False)
            # Set  the portfolio relationship
            project.portfolio = portfolio
            project.save()
            
            # Redirect back to the portfolio detail page
            return redirect('portfolio-detail', pk)
    context = {'form': form, 'action': 'Add', 'object_type': 'Project'}
    return render(request, 'portfolio_app/project_form.html', context)
