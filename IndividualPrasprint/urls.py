from django.urls import path
from IndividualPrasprint.views import show_html

app_name = 'IndividualPrasprint'

urlpatterns = [
    path('', show_html, name='show_html'),
]