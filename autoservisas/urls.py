from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('automobiliai/', views.automods, name='automods-all'),
    path('automobiliai/<int:id>', views.auto_detail, name='auto-detail')
]
