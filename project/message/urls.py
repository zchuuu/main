from django.urls import path
from . import views

urlpatterns = [
    path('find/category/<str:slug>/', views.category_page_find),
    path('complete/category/<str:slug>/', views.category_page_complete),
    path('ask/category/<str:slug>/', views.category_page_ask),
    path('find/', views.findList.as_view()),
    path('find/<int:pk>/', views.findDetail.as_view()),
    path('ask/', views.askList.as_view()),
    path('ask/<int:pk>/', views.askDetail.as_view()),
    path('complete_post/', views.completeList.as_view()),
    path('complete_post/<int:pk>/', views.complete_post, name='complete_post'),
    path('create_findPost/', views.FindPostCreate.as_view()),
    path('create_askPost/', views.AskPostCreate.as_view()),
]
