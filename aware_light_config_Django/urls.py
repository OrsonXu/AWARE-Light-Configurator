"""aware_light_config_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from django.views.generic import TemplateView

from App01 import database_operations, general

urlpatterns = [
    path('test_connection/', database_operations.test_connection),
    path('get_token/', general.get_token),
    path('initialize_database/', database_operations.initialize_database),
    path('save_json_file/', general.save_json_file),
    path('add_count/', general.add_count),
    re_path(r'.*', TemplateView.as_view(template_name='index.html')),
]
