from django.urls import path
from apps.anesthesiologist import views

app_name = 'anesthesiologist'

urlpatterns = [
    path('anesthesiologistinfo', views.anesthesiologistinfo, name='create_anesthesiologist'),
    path('', views.show, name='showanesthesiologist'),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
    ]