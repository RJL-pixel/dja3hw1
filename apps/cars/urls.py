from django.urls import path

from .views import CarListCreateView, CarRetrieveDestrouUpdatrView
urlpatterns = [

    path('', CarListCreateView.as_view()),
    path('/<int:pk>', CarRetrieveDestrouUpdatrView.as_view())

]