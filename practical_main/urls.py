from django.urls import path
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.userprofile, name='userprofile'),
    # path('/register', views.register, name='register'),
    path('register/', views.register, name='register'),
    path('display/', views.display, name='display'),
    path('delete/<int:pk>',views.delete, name='delete-person'),
]