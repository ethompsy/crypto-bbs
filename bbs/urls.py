from django.conf.urls import patterns, include, url
from django.contrib import admin
from bbs import views

urlpatterns = patterns('',
	# Django Admin (why not?)
    url(r'^admin/', include(admin.site.urls)),
    # API URLs
    url(r'^board/$', views.boardAPI, name='board-api'),
    url(r'^board/(?P<key>\d+)/$', views.boardAPI, name='board-api'),
    url(r'^post/$', views.postAPI, name='post-api'),
    url(r'^post/(?P<key>\d+)/$', views.postAPI, name='post-api'),
    # The Board:
    url(r'^$', views.board, name='board'),
    url(r'^(?P<pk>\d+)/$', views.BoardDetailView.as_view(), name='board-detail'),
)
