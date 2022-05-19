from django import forms
from .models import UploadImage


class UploadImageForm(forms.Form):
  title = forms.CharField(max_length=50)
  image = forms.ImageField()


class ImageUploadForm(forms.ModelForm):
  class Meta:
	  model = UploadImage
	  fields = ('description', 'document' )