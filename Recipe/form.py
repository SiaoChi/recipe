from django.forms import ModelForm
from django.forms import  inlineformset_factory
from django import forms
from myRecipe.models import Recipe , Material, Sauce, RecipeImage
from django_summernote.widgets import SummernoteWidget


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields= "__all__"
        exclude =['owner', 'created', 'id','user']
        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
            'source_link':forms.TextInput(attrs={'class': 'input'}),
            #這邊標示等於可以上傳多張圖 multiple
            # 'featured_image':forms.ClearableFileInput(attrs={'multiple': True,'name':'images'}),
            'detail':SummernoteWidget(),
        }
        labels = {
            'featured_image': '參考圖',
            'name':'菜名',
            'author':'作者',
            'tags':'分類',
            'detail':'作法',
            'source_link':'參考連結',

        }


    def __init__(self,*args,**kwargs):
        super(RecipeForm,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


MaterialFormSet = inlineformset_factory(Recipe, Material ,fields= ('name','unit',),
                                         extra=1, can_delete=False ,
                                   widgets = {'name':forms.TextInput(attrs={'class': 'input'}),
                                                 'unit':forms.TextInput(attrs={'class': 'input'}),

                                                    },
                                   labels= {
                                       'name':'名稱',
                                       'unit':'份量',
                                   }
                                        )




SauceFormSet = inlineformset_factory(Recipe, Sauce ,fields= ('name','unit',),extra=1, can_delete=False ,
                                   widgets = {'name':forms.TextInput(attrs={'class': 'input'}),
                                                 'unit':forms.TextInput(attrs={'class': 'input'}),

                                                    },
                                    labels = {
                                        'name': '名稱',
                                        'unit': '份量'
                                    }
                                     )
