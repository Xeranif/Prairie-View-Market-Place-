from django.urls import path

from . import views

app_name = "store"

urlpatterns = [
    path("", views.home, name="store_home"),
    path("items", views.product_all, name="all_items"),
    path("team", views.footer_team, name="footer_team"),
    path("privacy", views.footer_privacy, name="footer_privacy"),
    path("terms", views.footer_terms, name="footer_terms"),
    path("faq", views.footer_faq, name="footer_faq"),
    path("sellingaccount", views.footer_sellingaccount, name="footer_sellingaccount"),
    path("<slug:slug>", views.product_detail, name="product_detail"),
    path("shop/<slug:category_slug>/", views.category_list, name="category_list"),
]