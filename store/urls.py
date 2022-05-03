from django.urls import path

from . import views

app_name = "store"

urlpatterns = [
    path("", views.home, name="store_home"),
    path("items", views.product_all, name="all_items"),
    path("<slug:slug>", views.product_detail, name="product_detail"),
    path("shop/<slug:category_slug>/", views.category_list, name="category_list"),

]