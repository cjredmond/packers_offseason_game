from django.conf.urls import url
from django.contrib import admin
from roster.views import IndexView, FreeAgentView, ReSignView, DraftView, DraftPlayerView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^free-agents/$', FreeAgentView.as_view(), name='free_agent_view'),
    url(r'^re-sign/$', ReSignView.as_view(), name='resign_view'),
    url(r'^draft/(?P<pk>\d+)/$', DraftView.as_view(), name='draft_view'),
    url(r'^draft/(?P<pk>\d+)/player/$', DraftPlayerView.as_view(), name='draft_player_view')
]
