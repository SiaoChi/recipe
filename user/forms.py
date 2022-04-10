from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class registerForm(UserCreationForm):
    #這裡可以加入field的條件

    class Meta:
        model = User
        fields=['username','email','password1','password2']

        labels = {
            'username':'使用者名稱',
            'email':'信箱',
            'password1':'密碼',
            'password2':'確認密碼',

        }

    def __init__(self,*args,**kwargs):
        super(registerForm,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


