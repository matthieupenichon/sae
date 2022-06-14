from django . urls import path
from . import views

urlpatterns = [
    path ('', views.index , name ='index') ,
    path ('machines/', views.machine_list_view , name ='machines') ,
]

from django . urls import path
from . import views

urlpatterns = [
    path ('', views.index , name='index') ,
    path ('machines/',
        views.machine_list_view ,
        name ='machines') ,
    path ('machine/<pk>',
        views.machine_detail_view ,
        name='machine-detail'),
    path ('personne/',
        views.personne_list_view ,
        name ='personne') ,
    path ('personne/<pk>',
        views.personne_detail_view ,
        name='personne-detail'),
]