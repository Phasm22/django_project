from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Connect path to portfolio_app urls
    # include urls from portfolio_app
    path('', include('portfolio_app.urls')),
]