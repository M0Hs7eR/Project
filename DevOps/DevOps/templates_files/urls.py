from django.urls import path

from .views import Demend, Geography, HomePage, LastVacancy, Skills


urlpatterns = [
    path('', HomePage, name='home'),
    path('demend/', Demend, name='demend'),
    path('geography/', Geography, name='geography'),
    path('skills/', Skills, name='skills'),
    path('lastVacancy/', LastVacancy, name='lastVacancy'),
]