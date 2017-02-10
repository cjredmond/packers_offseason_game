from django.conf.urls import url
from django.contrib import admin
from roster.views import IndexView, FreeAgentView, ReSignView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^free-agents/$', FreeAgentView.as_view(), name='free_agent_view'),
    url(r'^re-sign/$', ReSignView.as_view(), name='resign_view'),
]
