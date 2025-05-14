from django.urls import path

from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.main, name="root"),
    path("<int:page>", views.main, name="root_paginate"),
    path("author/<str:fullname>/", views.author_detail, name="author_detail"), 
    path("tag/<str:tag_name>/", views.quotes_by_tag, name="quotes_by_tag"),  
    path("tag/<str:tag_name>/<int:page>/", views.quotes_by_tag, name="quotes_by_tag_paginate"),

]
