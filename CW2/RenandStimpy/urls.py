from django.urls import path
from . import views
#references the views in the app, RenandStimpy
urlpatterns=[path('',views.index,name='index'),
 path('song',views.happyjoy,name='index'),
 path('whenIsawRenandStimpy',views.young, name='index')]