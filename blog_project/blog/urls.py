from django.urls import path
from .views import post_list, tag_list, post_detail, tag_detail



urlpatterns = [
    path("", post_list, name = "post_list_url"),
    path('tags/', tag_list, name = "tag_list_url"),
    path('posts/<int:pk>/', post_detail, name ="post_detail_url" ),
    path('tags/<int:pk>/', tag_detail, name = "tag_detail_url")
]




