from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST
from .forms import UserForm 
from django.contrib.auth import login
from mypage.forms import ProfileForm
def index(request):
    
    return render(request,'accounts/index.html')
# Create your views here.
def regist(request):
    # バリデーション失敗時のページ到着も考慮してデータを取得
    form_data = request.session.pop('form_data',None)
    form = UserForm(form_data)
    context ={
        "form":form,
    }
    return render(request,'accounts/regist.html',context)
@require_POST
def regist_confirm(request):
    # 受け取ったrequestのPOSTのデータを取得
    form = UserForm(request.POST)
    context = {
        "form":form,
    }
    # バリデーションでうまく行けば確認画面を表示
    if form.is_valid():
        #フォームデータをセッションに保存
        request.session['form_data']=request.POST
        return render(request,'accounts/regist_confirm.html',context)
    # バリデーション失敗時にはフォームに戻る
    return render(request,'accounts/regist.html',context)

@require_POST
def regist_save(request):
    form_data = request.session.pop('form_data',None)
    form = UserForm(form_data)
    if form.is_valid():
        user = form.save(commit=False)
        profile = ProfileForm(commit = False)
        profile.save()
        user.profile_id = profile.id
        user.save()
        login(request,user,backend="django.contrib.auth.backends.ModelBackend")
        return redirect("accounts:index")
    context = {
        "form":form,
    }
    return render(request,'accounts/regist_confirm',context)
        

