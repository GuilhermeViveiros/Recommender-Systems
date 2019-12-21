# dappx/models.py
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    portfolio_site = models.URLField(blank=True)
    
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    
    def __str__(self):
        return self.user.username

class Movie(models.Model):
    idd = models.CharField(max_length=150)
    title = models.TextField()
    year = models.CharField(max_length=150)
    month = models.CharField(max_length=150)
    vote_average = models.CharField(max_length=150)
    adult = models.TextField()
    popularity = models.CharField(max_length=150)
    belongs_to_collection = models.CharField(max_length=150)
    spoken_languages = models.TextField()
    profit = models.CharField(max_length=150)
    genres = models.TextField()
    original_language = models.TextField()
    original_title = models.TextField()
    production_companies = models.TextField()
    production_countries = models.TextField()
    runtime = models.CharField(max_length=150)
    vote_count = models.CharField(max_length=150)
    revenue = models.CharField(max_length=150)
    animation = models.CharField(max_length=150)
    comedy = models.CharField(max_length=150)
    family = models.CharField(max_length=150)
    adventure = models.CharField(max_length=150)
    fantasy = models.CharField(max_length=150)
    romance = models.CharField(max_length=150)
    drama = models.CharField(max_length=150)
    action = models.CharField(max_length=150)
    crime = models.CharField(max_length=150)
    thriller = models.CharField(max_length=150)
    horror = models.CharField(max_length=150)
    history = models.CharField(max_length=150)
    scienceFiction = models.CharField(max_length=150)
    mystery = models.CharField(max_length=150)
    war = models.CharField(max_length=150)
    foreign = models.CharField(max_length=150)
    music = models.CharField(max_length=150)
    documentary = models.CharField(max_length=150)
    western = models.CharField(max_length=150)
    tvMovie = models.CharField(max_length=150)
    cluster = models.TextField()  
    
    def __str__(movieself):
        return movieself.idd