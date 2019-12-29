from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from  polls.TopN import topN,similarity_movies

@login_required
def home(request):
    movies = topN(12);
    return render(request, 'polls/index.html', {"movies" : movies});