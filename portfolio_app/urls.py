from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('',  views.index, name='login'),
path('', views.index, name='logout'),

# view for viewing all students
path('students/', views.StudentListView.as_view(), name='students'),
# view for viewing student details
path('student/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),
# view for viewing portfolio
path('portfolio/<int:pk>/', views.PortfolioDetailView.as_view(), name='portfolio-detail'),
#view for updating portfolio
path('portfolio/<int:pk>/update/', views.PortfolioUpdateView.as_view(), name='portfolio-update'),
# create project
path('portfolio/<int:pk>/project/create/', views.createProject, name='create-project'),
# update project
path('project/<int:pk>/update/', views.ProjectUpdateView.as_view(), name='update-project'),
# delete project
path('project/<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='delete-project'),
]
