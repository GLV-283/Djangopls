from django.shortcuts import render

from catalog.models import filmini

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_films = filmini.objects.all().count()

    context = {
        'num_books': num_films,

    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)