from django.contrib import admin
from django.urls import path, include

#staticを追加 
from django.conf.urls.static import static

# settingsを追加
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # appを紐ずける
    path('', include('app.urls')),
]

# プロジェクトURLにappアプリを指定
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)