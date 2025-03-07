from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import event_list

from .views import (
    Home, student_signup, student_login,campus_map,Main,mvj_view,hostel,
    teacher_signup, teacher_login, logout_view,student_profile,event_list,submit_review,kjc_view,about,school
)

urlpatterns = [
    path('', Main, name='Main'),
    path('cmr/', Home, name='home'),
    path('signup/student/', student_signup, name="student_signup"),
    path('signup/teacher/', teacher_signup, name="teacher_signup"),
    path('login/student/', student_login, name="student_login"),
    path('login/teacher/', teacher_login, name="teacher_login"),
    path('logout/', logout_view, name="logout"),
    path('profile/student/', student_profile, name="student_profile"),
    path('campus-map/', campus_map, name='campus_map'),
    path("events/", event_list, name="event_list"),
    path("submit-review/", submit_review, name="submit_review"),
    path("kjc/", kjc_view, name="kjc_view"),
    path("mvj/", mvj_view, name="mvj_view"),
    path("about/", about, name="about"),
    path("school/", school, name="school"),
    path("hostel/", hostel, name="hostel"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)