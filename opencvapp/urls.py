from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from . views import ImageView

urlpatterns = [
 url(r'^blurface/$', views.blurface, name='blurface'),
 url('rest/', ImageView.as_view(), name='image_view')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)