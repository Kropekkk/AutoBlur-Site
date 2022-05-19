from django.shortcuts import render
from .forms import UploadImageForm, ImageUploadForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .blur import blur

def blurface(request):
  form = ImageUploadForm(request.POST, request.FILES)
  if request.method == 'POST':
     if form.is_valid():
        post = form.save(commit=False)
        post.save()
 
        imageURL = settings.MEDIA_URL + form.instance.document.name
        blur(settings.MEDIA_ROOT_URL + imageURL)
 
        return render(request, 'opencvapp/blurface.html', {'form':form, 'post':post})
  else:
     form = ImageUploadForm()
  return render(request, 'opencvapp/blurface.html',{'form':form})