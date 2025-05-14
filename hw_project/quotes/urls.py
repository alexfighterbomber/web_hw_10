from django.urls import path

from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.main, name="root"),
    path("<int:page>", views.main, name="root_paginate"),
    path("author/<str:fullname>/", views.author_detail, name="author_detail"), 
    path("tag/<str:tag_name>/", views.quotes_by_tag, name="quotes_by_tag"),  
    path("tag/<str:tag_name>/<int:page>/", views.quotes_by_tag, name="quotes_by_tag_paginate"),
    path('quotes/add_user_author/', views.add_user_author, name='add_user_author'),
    path('quotes/add_user_quote/', views.add_user_quote, name='add_user_quote'),
    path('quotes/contributions/', views.user_contributions, name='user_contributions'),
]
