from django.contrib import admin
from django.urls import path, include
urlpatterns = [
path('admin/', admin.site.urls),
#connect path to portfolio_app url s
path('', include('portfolio_app.urls')),
]
