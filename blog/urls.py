from django.urls import path
from blog.views import HomeView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView




urlpatterns = [
    path('post/', HomeView.as_view(), name='blog_home_page'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='blog_detail_page'),
    path('post/new/', PostCreateView.as_view(), name='blog_new_page'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='blog_update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name='blog_delete'),
]
 