from django.urls import path
from skip.views import index, search, delete, insert


urlpatterns = [
    path("", index, name = "index"),
    path("search/", search, name = "search"),
    path("delete/", delete, name = "delete"),
    path("insert/", insert, name = "insert"),

]
