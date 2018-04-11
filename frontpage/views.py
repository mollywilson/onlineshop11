from django.views import generic
from .models import Album

class IndexView(generic.ListView):
    template_name = 'frontpage/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'frontpage/detail.html'