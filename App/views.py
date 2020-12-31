from django.shortcuts import render, redirect

from mal import AnimeSearch
from . import models

# Create your views here.
def index(request):
  if request.method == 'POST':
    search = request.POST['search']
    results = AnimeSearch(search).results
    if len(results)>0:
      a = results[0]
      anime = models.Anime(title=a.title, image_url=a.image_url)
      anime.save()

  anime = models.Anime.objects.all()
  context = {'anime': anime}
  return render(request, 'App/index.html', context)

def change_status(request, pk, status):
  anime = models.Anime.objects.get(id=pk)
  anime.status = {'1':'Planning to Watch', '2':'Watching', '3':'Completed'}[status]
  anime.save()

  return redirect('/')