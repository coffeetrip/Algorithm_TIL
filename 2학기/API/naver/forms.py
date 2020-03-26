
from django import forms
from django.core.validators import RegexValidator
from .widgets import NaverMapPointWidget


class PostForm(forms.Form):
    point = forms.CharField(validators=[RegexValidator('[+-]?[\d\.]+,[+-]?[\d\.]+$')], widget=NaverMapPointWidget)