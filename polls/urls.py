from django.urls import path
from .import views

app_name = 'polls'

''' 调用传统的方式
urlpatterns = [
        path("", views.index, name = "index"),
        path("<int:question_id>/", views.detail, name="detail"),
        path("<int:question_id>/results/", views.results, name="results"),
        path("<int:question_id>/vote/", views.vote, name="vote"),
        ]
'''

# 调用generic 模板
urlpatterns = [
    path("", views.IndexView.as_view(), name = 'index'),
    path("<int:pk>/", views.DetailView.as_view(), name = 'detail'),
    path("<int:pk>/results/", views.ResultView.as_view(), name = 'results'),
    path("<int:question_id>/vote/", views.vote, name = "vote"),
]