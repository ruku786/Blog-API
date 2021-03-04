from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import RegisterView,VerifyEmail,PostList,PostDetail,CommentDetail,CommentList

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
    
    path('register/', RegisterView.as_view(), name="register"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('comments/', CommentList.as_view()),
    path('comments/<int:pk>/', CommentDetail.as_view()),

]

