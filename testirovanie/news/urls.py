from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewsDetailVeiw.as_view(), name='news-detail'),
    #path('counter/<int:pk>/', views.ArticleCounterRedirectView.as_view(), name='news-detail'),
    path('<int:pk>/update', views.NewsUpdateVeiw.as_view(), name='news-update'),
    path('<int:pk>/delete', views.NewsDeleteVeiw.as_view(), name='news-delete'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),





]
