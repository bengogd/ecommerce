from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:product_id>', views.product_detail_view, name='listing'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)