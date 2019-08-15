from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

from .models import AdvUser, user_registrated, SubRubric, SuperRubric


class ChangeUserInfoForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Email address')

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'first_name', 'last_name', 'send_message')


class RegisterUserForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Email address')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput,
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Password (repeat)', widget=forms.PasswordInput,
                                help_text='Enter password again')

    def clean_password(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError('Password do not match', code='password_mismatch')}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = False
        user.is_activated = False
        if commit:
            user.save()
        user_registrated.send(RegisterUserForm, instance=user)
        return user

    class Meta:
        model = AdvUser
        fields = {'username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'send_message'}


class SubRubricForm(forms.ModelForm):
    super_rubric = forms.ModelChoiceField(queryset=SuperRubric.objects.all(), empty_label=None,
                                          label='Super_rubric', required=True)

    class Meta:
        model = SubRubric
        fields = '__all__'


class SearchForm(forms.Form):
    keyword = forms.CharField(required=False, max_length=20, label='')
