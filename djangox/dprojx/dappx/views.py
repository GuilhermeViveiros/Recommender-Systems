# dappx/views.py
from django.shortcuts import render
from dappx.forms import UserForm #,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from dappx.models import Movie
import csv


def index(request):
    return render(request,'dappx/index.html',{'movie':Movie})
    
@login_required
def special(request):
    return HttpResponse("You are logged in !")
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
    
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        #profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid(): # and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            #profile = profile_form.save(commit=False)
            #profile.user = user
            #if 'profile_pic' in request.FILES:
             #   print('found it')
              #  profile.profile_pic = request.FILES['profile_pic']
            #profile.save()
            registered = True
        else:
            print(user_form.errors) #,profile_form.errors)
    else:
        user_form = UserForm()
        #profile_form = UserProfileInfoForm()
    return render(request,'dappx/registration.html',
                          {'user_form':user_form,
                           #'profile_form':profile_form,
                           'registered':registered})
                           
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'dappx/login.html', {})


def movies_upload(request):
    #template = "register.html"
    #data = Movie.objects.all()

    #prompt = {
     #   'order': 'idd, title, year, month, vote_average, adult, popularity, belongs_to_collection, spoken_languages, profit, genres, original_language, original_title, production_companies, production_countries, runtime, vote_count, revenue, animation, comedy, family, adventure, fantasy, romance, drama, action, crime, thriller, horror, history, scienceFiction, mystery, war, foreign, music, documentary, western, tvMovie, cluster'
        #'movies': data
      #        }
    #if request.method == "GET":
     #   return render(request, template, prompt)

    #if request.method == 'POST':
    #csv_file = request.FILES['movie_data_cleaned.csv']
    #data_set = csv_file.read().decode('UTF-8')

    #io_string = io.StringIO(data_set)
    #next(io_string)

    with open("/home/sofia/djangox/dprojx/dappx/movie_data_cleaned.csv") as f:
        for column in csv.reader(f,delimiter=',', quotechar="|"): #io_string, delimiter=',', quotechar="|"):
            _, created = Movie.objects.update_or_create(
                idd = column[0],
                title = column[1],
                year = column[2],
                month = column[3],
                vote_average = column[4],
                adult = column[5],
                popularity = column[6],
                belongs_to_collection = column[7],
                spoken_languages = column[8],
                profit = column[9],
                genres = column[10],
                original_language  = column[11],
                original_title = column[12],
                production_companies = column[13],
                production_countries = column[14],
                runtime = column[15],
                vote_count = column[16],
                revenue = column[17],
                animation = column[18],
                comedy = column[19],
                family = column[20],
                adventure = column[21],
                fantasy = column[22],
                romance = column[23],
                drama = column[24],
                action = column[25],
                crime = column[26],
                thriller = column[27],
                horror = column[28],
                history = column[29],
                scienceFiction = column[30],
                mystery = column[31],
                war = column[32],
                foreign = column[33],
                music = column[34],
                documentary = column[35],
                western = column[36],
                tvMovie = column[37],
                cluster = column[38],
            )

    movies = Movie.objects.all()

    return render(request, 'dappx/movies.html', {'movies':movies})