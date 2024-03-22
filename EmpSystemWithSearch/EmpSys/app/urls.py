from django.urls import path
from app import views

urlpatterns = [
    path('',views.index, name='index'),
    path('addemp/',views.addemp, name='addemp'),
    path('viewempdata/',views.viewempdata,name='viewempdata'),
    path('removeempdata/<int:id>/',views.removeempdata,name='removeemp')
]