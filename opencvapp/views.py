from django.shortcuts import render
from .forms import ImageUploadForm
from django.conf import settings
from .blur import blur

def main(request):
    return render(request, "opencvapp/main.html", {
    })

def blurface(request):
  form = ImageUploadForm(request.POST, request.FILES)
  if request.method == 'POST':
     if form.is_valid():
        post = form.save(commit=False)
        post.save()
        
        sliderInfo = form.instance.slider
        imageURL = settings.MEDIA_URL + form.instance.document.name
        blur(settings.MEDIA_ROOT_URL + imageURL, sliderInfo)
 
        return render(request, 'opencvapp/blurface.html', {'form':form, 'post':post})
  else:
     form = ImageUploadForm()
  return render(request, 'opencvapp/blurface.html',{'form':form})