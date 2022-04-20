from django.shortcuts import render, redirect
from .forms import registerForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from myRecipe.models import Recipe
#讓登入的人才能看到的功能
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def registerUser(request):
    page = 'register'
    form = registerForm()

    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, '註冊成功')
            login(request, user)
            return redirect('home')






        else:
            messages.error(
                request, 'An error has occurred during registration')

    context = {'page':page, 'form':form}

    return render(request, 'login_register.html',context)


def loginUser(request):
    #page的定義是為了確認user是否有login，請看 login_register.html 第五行
    page = 'login'

    #如果user有在backend中，幫user返回account
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)

        except:
            messages.error(request, '使用者不存在')


        user =authenticate(request, username=username,password=password)

        if user is not None:
            login(request ,user)
            messages.success(request, '登入')
            return redirect('home')

        else:
            messages.error(request,'使用者名稱或是密碼不正確')

    #對應urls的網址對應到的views.loginUser Html
    return render(request, 'login_register.html')

def logoutUser(request):
    logout(request)
    messages.success(request, '使用者登出')
    return redirect('login')





