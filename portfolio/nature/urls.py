from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from nature import views
from django.views.generic.base import RedirectView
urlpatterns = [ 
    path('banyan/', views.Banyantree.as_view()),
    path('peepal/', views.Peepaltree.as_view()),
    path('neem/', views.Neemtree.as_view()),
    path('trees/',views.trees.as_view()),
    path('', RedirectView.as_view(url="trees/")),  
]