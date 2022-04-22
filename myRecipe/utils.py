from django.db.models import Q
from .models import Recipe ,Tag
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def searchRecipe(request):

    search_query=''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(name__icontains=search_query)

    recipes = Recipe.objects.distinct().filter(
        Q(name__icontains = search_query)|
        Q(material__icontains= search_query) |
        Q(author__icontains= search_query)|
        Q(tags__in=tags)
                                  )

    context = {'recipes':recipes, 'search_query':search_query}
    return recipes, search_query


def searchMyRecipe(request):

    search_query=''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(name__icontains=search_query)
    user = request.user
    recipes = user.recipe_set.distinct().filter(
        Q(name__icontains = search_query)|
        Q(material__icontains= search_query) |
        Q(author__icontains= search_query)|
        Q(tags__in=tags)
                                  )

    context = {'recipes':recipes, 'search_query':search_query}
    return recipes, search_query