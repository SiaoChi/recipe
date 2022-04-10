from django.contrib import admin
from .models import Recipe, Material,Tag, Sauce, RecipeImage
# from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
# class InlineRecipe():

class MaterialInline(admin.TabularInline):
    model = Material

class SauceInline(admin.TabularInline):
    model = Sauce

class ImageInline(admin.TabularInline):
    model = RecipeImage

# class SummerAdmin(SummernoteModelAdmin):
#     summernote_fields ="__all__"

class RecipeAdmin(admin.ModelAdmin):
    inlines = [ImageInline, MaterialInline, SauceInline]
    list_display = ['name', 'user']
    readonly_fields = ['user', 'created']
    raw_id_fields = ['user']


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag)

