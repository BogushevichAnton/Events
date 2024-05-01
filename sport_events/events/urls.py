from django.urls import path
from django.views.i18n import JavaScriptCatalog

from .views import *

urlpatterns = [
    path('', EventsView.as_view(), name='events-list'),

    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catalog'),

    path('<int:pk>/', EventsDetail.as_view(), name='events-detail'),
    path('add/', EventsAdd.as_view(), name='events_add'),
    path('<int:pk>/delete/', EventsDelete.as_view(), name='events-delete'),
    path('<int:pk>/update/', EventsUpdate.as_view(), name='events-update'),

]