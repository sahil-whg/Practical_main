from django.urls import path
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.userprofile, name='userprofile'),
    path('display/', views.display, name='display'),
    path('filter/', views.filter, name='filter'),
    path('delete/<int:pk>',views.delete, name='delete-person'),
]