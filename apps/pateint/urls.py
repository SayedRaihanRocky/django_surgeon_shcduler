from django.urls import path
from apps.pateint import views

app_name = 'pateint'

urlpatterns = [
    path('', views.show, name='showpateint'),
    path('pateintinfo', views.pateintinfo, name='pateintinfo'),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
    ]