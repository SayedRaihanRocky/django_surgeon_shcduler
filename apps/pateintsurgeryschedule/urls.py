from django.urls import path
from apps.pateintsurgeryschedule import views

app_name = 'pateintsurgeryschedule'

urlpatterns = [
    path('pateintsurgeryscheduleinfo', views.create_pateintsurgeryschedule, name='createpateintsurgeryschedule'),
    path('', views.show, name='showpateintsurgeryschedule'),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
    ]