from django import forms
from .models import Blog,Comment
from django.contrib.auth.models import User



class BlogForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields = ['title','description','author']


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['blog','comment','comment_by']


class UserSignupForm(forms.ModelForm):
	password1 = forms.CharField(label='Password',widget=forms.PasswordInput)

	password2 = forms.CharField(label='Password conformation', widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ('username','email')
	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')

		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("password don;t match")
			return password2

	def save(self, commit=True):
		user = super(UserSignupForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user


