from django.shortcuts import render
from django.views import generic
from catalog.models import filmini
from django.shortcuts import get_object_or_404



def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_films = filmini.objects.all().count()

    context = {
        'num_films': num_films,

    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class filminiListView(generic.ListView):
    model = filmini
    context_object_name = 'filmini_list'  # your own name for the list as a template variable
    #queryset = filmini.objects.filter(title__icontains='war')[:5]  # Get 5 books containing the title war
    template_name = 'filmini_list.html'# Specify your own template name/location
    paginate_by = 20

class filminiDetailView(generic.DetailView):
    model = filmini
    #template_name = 'filmini_detail.html'

    def book_detail_view(request, primary_key):
        try:
            film = filmini.objects.get(pk=primary_key)
        except filmini.DoesNotExist:
            raise Http404('film does not exist')

        return render(request, 'catalog/filmini_detail.html', context={'film': film})

    # def book_detail_view(request, primary_key):
    #     film = get_object_or_404(filmini, pk=primary_key)
    #     return render(request, 'catalog/filmini_detail.html', context={'film': film})

