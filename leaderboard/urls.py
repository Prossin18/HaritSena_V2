from django.urls import path
from . import views

urlpatterns = [
    path('', views.leaderboard, name="leaderboard"),
    path('rewards/', views.rewards, name="rewards")
]
