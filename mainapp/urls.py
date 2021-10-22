from django.urls import path
from .views import *
urlpatterns=[
    path('',index,name='home'),
    path('ishchi/',ishchi,name='ishchi'),
    path('lematizatsiya/',lematizatsiya,name='lematizatsiya'),
    path('morfemik_tahlil/',morfemik_tahlil,name='morfemik_tahlil'),
    path('stemming/',stemming,name='stemming'),
    path('asosdosh_sozlar/',asosdosh_sozlar,name='asosdosh_sozlar'),
]