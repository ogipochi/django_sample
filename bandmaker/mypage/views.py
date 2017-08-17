from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.generic.list import ListView
from django.utils import timezone
from django.contrib.auth.models import User
from mypage.models import Profile 
from .forms import ProfileForm

# Create your views here.
@login_required
def index(request):
    # idからユーザ検索
    # ユーザからProfileを検索
    profile = request.user.profile
    user = request.user
    context={
        'profile':profile,
        'user':user,
    }
    return render(request,'mypage/index.html',context)
@login_required
def edit(request):
    # sessionにデータがあれば取得
    form_data = request.session.pop('profile_data',None)
    # sessionからデータを取得できればフォームに入力
    form = ProfileForm(form_data)
    context = {
        "form":form
    }
    return render(request,'mypage/edit.html',context)

@login_required
@require_POST
def edit_confirm(request):
    form = ProfileForm(request.POST)
    context = {
        "form":form,
    }    
    if form.is_valid():
        request.session["profile_data"] = request.POST
        return render(request,'mypage/edit_confirm.html',context)
    return render(request,'mypage/edit.html',context)
@login_required
@require_POST
def edit_save(request):
    # フォームデータをセッションから取得
    form_data = request.session.pop('profile_data',None)
    profile = Profile.objects.get(id=request.user.profile.id)

    form = ProfileForm(form_data,instance = profile)
    if form.is_valid():
        profile = form.save(commit=False)
        profile.save()
        return redirect("mypage:index")
    context = {
        "form":form
    }
    return render(request,'mypage/edit_confirm',context)

    
    
    