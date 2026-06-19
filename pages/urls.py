from django.urls import path

from pages.views import HomePageView, CategoryListView


urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('<str:category>/', CategoryListView.as_view(), name='category_list'),
]