from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
from .forms import MovieForm


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})


def movie_create(request):
    form = MovieForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('movie_list')
    return render(request, 'movies/movie_form.html', {'form': form})


def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    form = MovieForm(request.POST or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('movie_list')
    return render(request, 'movies/movie_form.html', {'form': form})


def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movie_list')
    return render(request, 'movies/movie_confirm_delete.html', {'movie': movie})
