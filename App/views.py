from django.shortcuts import render

from mal import AnimeSearch

# Create your views here.
def index(request):
  if request.method == 'POST':
    search = request.POST['search']
    anime = AnimeSearch(search).results[0]
  return render(request, 'App/index.html')