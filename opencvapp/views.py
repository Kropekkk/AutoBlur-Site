from django.shortcuts import render
from .forms import ImageUploadForm
from django.conf import settings
from .blur import blur
from rest_framework.response import Response
from rest_framework import generics
from . serializers import ImageSerializer
from . models import UploadImage

class ImageView(generics.RetrieveAPIView):
   queryset = UploadImage.objects.all()

   def get(self, request, *args, **kwargs):
      queryset = self.get_queryset()
      serializer = ImageSerializer(queryset, many=True)
      return Response(serializer.data)

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