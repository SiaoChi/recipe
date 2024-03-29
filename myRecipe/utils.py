from django.db.models import Q
from .models import Recipe ,Tag
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def searchRecipe(request):

    search_query=''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    # tags = Tag.objects.filter(name__icontains=search_query)

    #所有的食譜
    recipes = Recipe.objects.distinct().filter(
        Q(name__icontains = search_query)|
        Q(material__name__icontains= search_query) |
        Q(author__icontains= search_query))
        # Q(tags__in=tags)

    context = {'recipes':recipes, 'search_query':search_query}
    return recipes, search_query


def searchMyRecipe(request):

    search_query=''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(name__icontains=search_query)
    user = request.user
    #使用者自己的食譜
    #如果沒有distinct()會有重複出現同一個食譜的狀況

    recipes = user.recipe_set.distinct().filter(
        Q(name__icontains = search_query)|
        Q(material__name__icontains= search_query) |
        Q(author__icontains= search_query)
        # Q(tags__in=tags)
                                  )

    context = {'recipes':recipes, 'search_query':search_query}
    return recipes, search_query

def paginatorRecipe(request, recipes, results):
    page = request.GET.get('page')  # page等於網頁上的 /?page="num"
    recipes = recipes.order_by('id') #要加入order_by不然會出現unorderedObjectListWarning的error
    paginator = Paginator(recipes, results)

    # 因為user enter from Nav, but nav is not integer page (url=project), so we have to direct Pagenotinterget to page 1
    try:
        recipes = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        recipes = paginator.page(page)
    except EmptyPage:  # 頁數太大（沒有這一頁）
        page = paginator.num_pages  # num_pages = 最後一頁
        recipes = paginator.page(page)

    leftIndex = (int(page) - 3)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 4)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, recipes