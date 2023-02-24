from django.urls import path
from .views import HomeView, PredictView, ResultView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('predict/', PredictView.as_view(), name='predict'),
    path('result/', ResultView.as_view(), name='result'),
]
