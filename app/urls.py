from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PredictView, PredictionResultView


urlpatterns = [
    path('predict/', PredictView.as_view(), name='predict'),
    path('predict/<str:prediction_id>', PredictionResultView.as_view(), name='prediction_result'),
]