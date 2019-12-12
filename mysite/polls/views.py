from django.shortcuts import get_object_or_404,render
from .models import Movie
from  . import TopN
from .TopN import topN



def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    
    #context = []
    #for i in movies
    movies = topN(3);

    return render(request, 'polls/index.html', {"list" : movies})

def search(request):

    inp_value = request.POST['movie_name']
    try:
        movie = Movie.objects.get(name=inp_value)
    except:
        inp_value = "An exception occurred"

    return render(request, 'polls/movie.html', {'context': inp_value});
    

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)