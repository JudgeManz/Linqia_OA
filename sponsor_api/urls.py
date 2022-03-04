from django.urls import path

from . import views 

urlpatterns = [
    path('vocab', views.Vocabulary.as_view()),
    path('prediction', views.Prediction.as_view())
]