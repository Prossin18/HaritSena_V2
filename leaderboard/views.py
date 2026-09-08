from django.shortcuts import render 
from django.http import HttpResponse

def leaderboard(request):
    return render(request, 'leaderboard/leaderboard.html')



# Create your views here.
