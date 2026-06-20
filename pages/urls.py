from django.urls import path

from pages.views import HomePageView, CategoryListView, search_list


urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('search/', search_list, name='search_list'),
    path('<str:category>/', CategoryListView.as_view(), name='category_list'),
]