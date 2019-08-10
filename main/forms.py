# from django import forms
# from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
# from django.contrib.auth.models import User


# class NewUserForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ("username",
#                   "first_name",
#                   "last_name",
#                   "email",
#                   "password1",
#                   "password2"
#                 )

    
#     def save(self, commit=True):
#         user = super(NewUserForm, self).save(commit=False)
#         user.username = self.cleaned_data['username']
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.email = self.cleaned_data['email']

#         if commit:
#             user.save()
#         return user