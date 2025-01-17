"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


# urlpatterns = [
#     path(r'^$', views.index_redirect, name='index_redirect'),
#     path(r'^crud/', include('crud.urls')),
#     path(r'^admin/', admin.site.urls),
# ]

from django.urls import path, include
# from django.contrib import admin
from django.contrib import admin
from . import views  # Ensure you import your views

urlpatterns = [
    path('', views.index_redirect, name='index_redirect'),  # Root URL
    path('crud/', include('crud.urls')),  # Include CRUD app URLs
    path('admin/', admin.site.urls),  # Admin URL
]

urlpatterns = [
    path('', views.index_redirect, name='index_redirect'),
    path('crud/', include('crud.urls')),
    path('admin/', admin.site.urls),
]