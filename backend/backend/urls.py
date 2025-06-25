from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Root welcome page
def home(request):
    return HttpResponse("✅ Welcome to the Blog API!")

urlpatterns = [
    path('', home),  # Root URL shows a simple welcome message
    path('admin/', admin.site.urls),  # Django Admin
    path('api/', include('blog.urls')),
  # All blog-related API routes
]
