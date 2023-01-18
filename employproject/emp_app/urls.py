from django.urls import path, include

from emp_app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('all_employ',views.all_employ,name='all_employ'),
    path('add', views.add, name='add'),
    path('remove', views.remove, name='remove')
]