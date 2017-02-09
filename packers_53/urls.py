from django.conf.urls import url
from django.contrib import admin
from roster.views import IndexView, FreeAgentView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^free-agents/$', FreeAgentView.as_view(), name='free_agent_view'),
]
