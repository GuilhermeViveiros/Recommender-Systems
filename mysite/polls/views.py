from django.shortcuts import get_object_or_404,render, redirect
import json as simplejson
from  . import TopN
from .ContentBased import ContentBased
from .RecommenderPearsonScript import user_based
from .TopN import topN,similarity_movies, info_movie, newUser, add_new_rate,User_max,get_movie,check_for_ratings_user_based
from .models import User_id


from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from .forms import UserLoginForm, UserRegisterForm

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "polls/login.html", context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)

        #id do utilizador, script python
        name_user, id_user = newUser();
        q = User_id(user_name = user.username , user_id = id_user);
        q.save()

        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "polls/singup.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')


def search(request):

    inp_value = request.POST['movie_name']
    #movie = Movie.objects.get(name=inp_value)
    movies = similarity_movies(inp_value)
    if(len(movies) == 0) :  
        movies = topN(12)
 
    return render(request, 'polls/index.html', {"movies": movies});


def results(request, movie):
    
    #info contains
    #movie_name #ano #mes #lingua #temas #runtime
    info = info_movie(movie)
    global_movie(movie)
    return render(request, 'polls/movie.html', {"context" : info})


def global_movie(movie):
    global movie_name
    if(not movie == "None"):
        movie_name = movie;
    return movie_name;


def index(request):
    #aqui é diferente, tenho que por os movies mais corretos para o user
    inp_value = request.POST['rate']

    if request.user.is_authenticated:
        username = request.user.username
        password = request.user.password

        q = User_id.objects.get(user_name = username);

    movie = ""
    #já tenho o user_name, o rating e movie_name, user_id
    #inp_value -> rating
    #movie -> filme
    movie_name = global_movie("None")
    movie = movie_name;
    #user -> username
    #meter na base de dados
    
    #user_name
    
    add_new_rate(q.user_id, inp_value, movie_name, 0);

    #após esse interiro fazer scipt python para povoar o rating table
        #chamar script
    
    user_name = "user_" + str(q.user_id)
    user_max = User_max()
   
    number_of_rates = check_for_ratings_user_based(q.user_id);
    if(number_of_rates > 20):
        movie, rate = user_based(user_max, user_name);
        movies = get_movie(movie);

    if(number_of_rates > 0 and number_of_rates < 20):
            movies = ContentBased(q.user_id);
            
    
    if(number_of_rates == 0):
        movies = TopN(12);

    print(movies);
    return render(request, 'polls/index.html', {"movies": movies});




def vote(request, question_id):
    
    return HttpResponse("You're voting on question %s." % question_id)



#não estou a por o length a aumentar