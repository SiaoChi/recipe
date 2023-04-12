from django.shortcuts import render, redirect
from .models import Recipe
# from django.contrib.auth import get_user_model
from Recipe.form import RecipeForm, MaterialFormSet, SauceFormSet
from django.contrib import messages
from .utils import searchRecipe, searchMyRecipe,paginatorRecipe
# from django.views.decorators.cache import cache_page
from PIL import Image
#hello world!




# Create your views here.

#首頁 食譜總覽
# @cache_page(60 * 15)
def Recipes(request):

     recipes, search_query = searchRecipe(request)
     custom_range, recipes = paginatorRecipe(request, recipes, 9)
     # recipes = Recipe.objects.all()
     # tags = Tag.objects.all()


     context = {'recipes':recipes , 'search_query':search_query,  'custom_range':custom_range}
     return render(request, 'home.html', context)


#瀏覽單一食譜
# @cache_page(60 * 15)
def singleRecipe(request,pk):
    recipe = Recipe.objects.get(id=pk)
    tags = recipe.tags.all()
    materials = recipe.material_set.all()
    sauces = recipe.sauce_set.all()
    images = recipe.recipeimage_set.all()

    context = {'tags':tags,
               'recipe': recipe,
               'materials':materials,
               'sauces':sauces,
               'images':images }
    return render(request, 'single-recipe.html', context)

#創造食譜表單
# @cache_page(60 * 15)
def CreateRecipe(request):
    form = RecipeForm()
    material_formset = MaterialFormSet()
    sauce_formset = SauceFormSet()

    if request.method == "POST":
        form = RecipeForm(request.POST,request.FILES)
        # print('test')
        # print(form)
        # print(request.FILES)

        if form.is_valid():
            #要記得form不能直接儲存，需要認列user
            recipe = form.save(commit=False)
            recipe.user = request.user   #request.user就能知道創造的人是誰
            recipe.save()


            #這邊要再次確認內容有formset並且屬於這個食譜
            material_formset= MaterialFormSet(request.POST, instance=recipe)
            sauce_formset = SauceFormSet(request.POST, instance=recipe)

            if material_formset.is_valid():
                material_formset.save()


            if sauce_formset.is_valid():
                sauce_formset.save()

        messages.success(request, 'was created!')
        return redirect('my-recipe')

    else:
        form = RecipeForm()
        material_formset = MaterialFormSet()
        sauce_formset = SauceFormSet()


    context = {'form' : form , 'material_formset': material_formset,
               'sauce_formset':sauce_formset }


    return render(request, 'recipe-form.html', context)



#修改食譜表單
# @cache_page(60 * 15)
def UpdateRecipe(request,pk):
    recipe = Recipe.objects.get(id=pk)
    form = RecipeForm(instance=recipe)
    material_formset = MaterialFormSet(instance=recipe)
    sauce_formset = SauceFormSet(instance=recipe)

    if request.method == "POST":
        form = RecipeForm(request.POST,request.FILES,instance=recipe)
        # print('test')
        print(form)
        # print(request.FILES)

        if form.is_valid():

            recipe = form.save()
            material_formset= MaterialFormSet(request.POST, instance=recipe)
            sauce_formset = SauceFormSet(request.POST, instance=recipe)

            if material_formset.is_valid():
                material_formset.save()

            if sauce_formset.is_valid():
                sauce_formset.save()

        messages.success(request, 'was updated!')
        return redirect('my-recipe')


    context = {'form' : form , 'material_formset': material_formset,
               'sauce_formset':sauce_formset }


    return render(request, 'recipe-form.html', context)

def DeleteRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    if request.method =="POST":
        recipe.delete()
        return redirect('my-recipe')

    context={'recipe':recipe}
    return render(request,'delete-recipe.html',context)

# @cache_page(60 * 15)
def UserRecipe(request):
    recipes, search_query = searchMyRecipe(request)
    #以下到utils
    # user = request.user
    # recipes = user.recipe_set.all()
    context = {'recipes':recipes , 'search_query':search_query }
    return render(request,'my-recipe.html', context)

# Recipe save to csv
import csv
from django.http import HttpResponse

def ExportCSV(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="recipes.csv"'

    writer = csv.writer(response)
    writer.writerow(['id', 'name', 'detail'])

    recipes = Recipe.objects.all()
    for recipe in recipes:
        writer.writerow([recipe.id,recipe.name , recipe.detail])

    return response

