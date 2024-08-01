from django.urls import path
from . import views


# urlpatterns= [
#     path(r'^$', views.index, name='index'),
#     path(r'^create$', views.create, name='create'),
#     path(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
#     path(r'^edit/update/(?P<id>\d+)$', views.update, name='update'),
#     path(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
# ]

urlpatterns = [
    path('', views.index, name='index/'),  # Root URL
    path('create', views.create, name='create'),  # Create URL
    path('edit/<int:id>', views.edit, name='edit'),  # Edit URL with an integer ID
    path('edit/update/<int:id>', views.update, name='update'),  # Update URL with an integer ID
    path('delete/<int:id>', views.delete, name='delete'),  # Delete URL with an integer ID
]

# urlpatterns = [
#     path('', views.index, name='index'),  # Root URL
#     path('create/', views.create, name='create'),  # Create URL
#     path('edit/<int:id>/', views.edit, name='edit'),  # Edit URL with an integer ID
#     # path('edit/update/<int:id>/', views.update, name='update'),  # Update URL with an integer ID
#     path('update/<int:id>/', views.update, name='update'),
#     path('delete/<int:id>/', views.delete, name='delete'),  # Delete URL with an integer ID
# ]
