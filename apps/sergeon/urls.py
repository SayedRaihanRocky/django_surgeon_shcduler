from django.urls import path
from apps.sergeon import views

app_name = 'surgeon'

urlpatterns = [
    path('surgeoninfo', views.surgeoninfo, name='create_surgeon'),
    path('', views.show, name='showsurgeon'),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
]