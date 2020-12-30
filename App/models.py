from django.db import models

# Create your models here.
class Anime(models.Model):
  title = models.CharField(max_length=300)
  image_url = models.CharField(max_length=300)
  episodes = models.IntegerField()
  completed_episodes = models.IntegerField(default=0)
  status = models.CharField(max_length=20, default='Planning to Watch', choices=((status, status) for status in ['Watching', 'Completed', 'Planning to Watch']))
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title