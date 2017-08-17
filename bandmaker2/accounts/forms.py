from django import forms
from accounts.models import MyUser

class UserForm(forms.ModelForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation',widget=forms.PasswordInput)
    class Meta:
        model = MyUser
        fields = ('email','first_name','last_name',)
    def clean_password2(self):
        # バリデーション済のデータを取得
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        # password1とpassword2が一致するかチェック
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    # save
    def save(self, commit=True):
        
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user