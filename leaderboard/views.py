from django.shortcuts import render 
from django.http import HttpResponse

def leaderboard(request):
    return render(request, 'leaderboard/leaderboard.html')


def rewards(request):
    return render(request, 'leaderboard/rewards.html')


# Create your views here.
