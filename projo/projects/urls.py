from django.urls import path
from .views import ProjectCreateView

urlpatterns = [
    path('create_project/', ProjectCreateView.as_view(), name='create_project'),
]
