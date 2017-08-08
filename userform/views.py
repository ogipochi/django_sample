from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.views.decorators.http import require_POST
from .models import UsersForm
# Create your views here.

def index(request):
    return render(request,'userform/index.html')

def regist_user(request):
    form_data = request.session.pop("form_data",None)
    form = UsersForm(form_data)
    context = {
        "form":form,
    }
    return render(request,'userform/regist.html',context)
# 確認画面
@require_POST
def regist_confirm(request):
    form = UsersForm(request.POST)
    context = {
        "form":form,
    }
    if form.is_valid():
        request.session['form_data'] = request.POST
        return render(request,'userform/confirm.html',context)
    return render(request,'userform/regist.html',context)

@require_POST
def regist_save(request):
    form_data = request.session.pop("form_data",None)
    form = UsersForm(form_data)
    if form.is_valid():
        user = form.save(commit=False)
        user.is_staff=True
        user.save()
        login(request,user,backend="django.contrib.auth.backends.ModelBackend")
        return redirect("userform:index")

    context = {
        "form":form,
    }
    return render(request,'uerform/confirm.html',context)


