from django.urls import path
from . import views
urlpatterns= [
    path('',views.index, name='index'),
    path('create/',views.create, name='create'),
    path('<int:diary_id>/',views.detail,name='detail'),
    path('<int:diary_id>/update',views.update,name='update'),
    path('<int:diary_id>/delete',views.delete,name='delete'),
]