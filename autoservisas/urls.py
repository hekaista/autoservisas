from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('automobiliai/', views.automobiliai, name='auto-all'),
    path('automobiliai/<int:auto_id>', views.automobilis, name='auto-one'),
    path('paslaugos/', views.paslaugos_list, name='paslaugos-list'),
    path('uzsakymai/', views.UzsakymaiListView.as_view(), name='uzsakymai-list'),
    path('uzsakymai/<uuid:pk>/', views.UzsakymasDetailView.as_view(), name='uzsakymas-detail'),
    path('search/', views.search, name='search'),

]
