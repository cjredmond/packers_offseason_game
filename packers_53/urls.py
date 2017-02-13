from django.conf.urls import url
from django.contrib import admin
from roster.views import IndexView, FreeAgentView, ReSignView, DraftView, DraftPlayerView, \
                         ReSignPlayerView, FreeAgentSignView, CutPlayerView, ResignCompleteView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^free-agents/$', FreeAgentView.as_view(), name='free_agent_view'),
    url(r'^re-sign/$', ReSignView.as_view(), name='resign_view'),
    url(r'^draft/(?P<pk>\d+)/$', DraftView.as_view(), name='draft_view'),
    url(r'^draft/(?P<pk>\d+)/player/$', DraftPlayerView.as_view(), name='draft_player_view'),
    url(r'^re-sign/(?P<pk>\d+)/player/$', ReSignPlayerView.as_view(), name='resign_player_view'),
    url(r'^free-agents/(?P<pk>\d+)/sign/$', FreeAgentSignView.as_view(), name='free_agent_sign_view'),
    url(r'^cut_player/(?P<pk>\d+)/$', CutPlayerView.as_view(), name='cut_player_view'),
    url(r'^re-sign/(?P<pk>\d+)/finished/$', ResignCompleteView.as_view(), name='resign_complete'),
]
