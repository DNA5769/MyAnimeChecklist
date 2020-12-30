from django.shortcuts import render

from mal import AnimeSearch
from . import models

# Create your views here.
def index(request):
  if request.method == 'POST':
    search = request.POST['search']
    a = AnimeSearch(search).results[0]

    anime = models.Anime(title=a.title, image_url=a.image_url, episodes=a.episodes)
    anime.save()

  anime = models.Anime.objects.all()
  context = {'anime': anime}
  return render(request, 'App/index.html', context)