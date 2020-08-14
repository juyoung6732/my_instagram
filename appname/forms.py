from django import forms
from .models import Post, CustomUser, Comment, Hashtag, Profile

#from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['location', 'content', 'image', 'hashtag_field']

class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['name']

class SigninForm(forms.ModelForm):
    username = forms.ModelChoiceField(
        queryset = CustomUser.objects.all(),
        label = "ID",
        required = True,
        widget = forms.TextInput(attrs={'class':'form-control'})
    )
    password = forms.ModelChoiceField(
        queryset = CustomUser.objects.all(),
        label = "PASSWORD",
        required = True,
        widget = forms.PasswordInput(attrs={'class':'form-control'})
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'password']

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'nickname', 'phone_number']

class CommentForm(forms.ModelForm):
    text = forms.ModelChoiceField(
        queryset = Comment.objects.all(),
        label = "comment",
        required = False,
        widget = forms.TextInput(attrs={'class':'form-control'})
    )
    class Meta:
        model = Comment
        fields = ['text']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']